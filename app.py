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
	'slash'
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
            'source': ['rock_song','one_ok_rock'],
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
            'trigger': 'go_back',
            'source': [
                'rock_song',
                'study_song'
            ],
            'dest': 'user'
        },
        {
            'trigger': 'advance',
            'source': [
                'one_ok_rock',
                'pink_noise',
                'slash'
            ],
            'dest': 'rock_song',
            'conditions': 'again'
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
