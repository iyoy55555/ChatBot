from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "1234567890987654321"
machine = TocMachine(
    states=[
        'user',
        'rock_song',
        'study_song',
	'one_ok_rock',
	'pink_noise',
	'slash',
        'choose_song_again',
        'help',
        'ask_emotion',
        'happy',
        'angry',
        'sad',
        'ask_again',
        'great_future',
        'happy_temp'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'rock_song',
            'conditions': 'is_going_to_rock_song'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'study_song',
            'conditions': 'is_going_to_study_song'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'ask_emotion',
            'conditions': 'is_going_to_ask_emotion'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'help',
            'conditions': 'need_help'
        },
        {
            'trigger': 'advance',
            'source': 'rock_song',
            'dest': 'one_ok_rock',
            'conditions': 'choose_one_ok_rock'
        },
        {
            'trigger': 'advance',
            'source': 'rock_song',
            'dest': 'pink_noise',
            'conditions': 'choose_pink_noise'
        },
        {
            'trigger': 'advance',
            'source': 'rock_song',
            'dest': 'slash',
            'conditions': 'choose_slash'
        },
        {
            'trigger': 'advance',
            'source': [
                'rock_song',
                'study_song'
            ],
            'dest': 'user',
            'conditions': 'again'
        },
        {
            'trigger': 'go_back',
            'source': ['help','great_future'],
            'dest':'user'
        },
        {
            'trigger': 'go_to_again',
            'source': [
                'one_ok_rock',
                'pink_noise',
                'slash',
                'study_song'
            ],
            'dest': 'choose_song_again',
        },
        {
            'trigger': 'advance',
            'source': 'choose_song_again',
            'dest': 'one_ok_rock',
            'conditions': 'choose_one_ok_rock'
        },	
        {
            'trigger': 'advance',
            'source': 'choose_song_again',
            'dest': 'pink_noise',
            'conditions': 'choose_pink_noise'
        },	
        {
            'trigger': 'advance',
            'source': 'choose_song_again',
            'dest': 'slash',
            'conditions': 'choose_slash'
        },
        {	
            'trigger': 'advance',
            'source': 'choose_song_again',
            'dest': 'rock_song',
            'conditions': 'again'
        },
        {	
            'trigger': 'advance',
            'source': 'choose_song_again',
            'dest': 'user',
            'conditions': 'ret'
        },
        {	
            'trigger': 'advance',
            'source': 'choose_song_again',
            'dest': 'study_song',
            'conditions': 'is_going_to_study_song'
        },
        {
            'trigger': 'advance',
            'source': 'ask_emotion',
            'dest': 'happy',
            'conditions': 'is_happy'
        },
        {
            'trigger': 'advance',
            'source': 'ask_emotion',
            'dest': 'angry',
            'conditions': 'is_angry'
        },
        {
            'trigger': 'advance',
            'source': 'ask_emotion',
            'dest': 'sad',
            'conditions': 'is_sad'
        },
        {
            'trigger': 'go_to_ask_again',
            'source': ['angry','sad'],
            'dest': 'ask_again'
        },
        {
            'trigger': 'advance',
            'source': 'ask_again',
            'dest': 'angry',
            'conditions': 'is_angry'
        },
        {
            'trigger': 'advance',
            'source': 'ask_again',
            'dest': 'sad',
            'conditions': 'is_sad'
        },
        {
            'trigger': 'advance',
            'source': 'ask_again',
            'dest': 'great_future',
            'conditions': 'want_great_future'
        },
        {
            'trigger': 'advance',
            'source': 'happy',
            'dest': 'great_future',
            'conditions': 'no'
        },
        {
            'trigger': 'advance',
            'source': 'happy',
            'dest': 'happy_temp',
            'conditions': 'yes'
        },
        {
            'trigger': 'advance',
            'source': 'happy_temp',
            'dest': 'happy'
        },
        {
            'trigger': 'return_happy',
            'source': 'happy_temp',
            'dest': 'happy'
        },
        {
            'trigger': 'advance',
            'source': 'great_future',
            'dest': 'user',
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
