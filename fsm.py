from transitions.extensions import GraphMachine

from utils import send_text_message, send_attachment_url, send_video_template,send_button_message,find_song,scrape_song


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
        self.check_from=None 

    def is_going_to_rock_song(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'rock song'
        return False

    def is_going_to_ask_emotion(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'talking'
        return False

    def ret(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'return'
        return False

    def need_help(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'help'
        return False

    def is_going_to_study_song(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'study song'
        return False

    def choose_one_ok_rock(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'one ok rock'
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == 'one ok rock'
        return False

    def choose_pink_noise(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'pink noise'
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == 'pink noise'
        return False

    def choose_slash(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'slash'
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == 'slash'
        return False

    def again(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go back'
        return False

    def is_happy(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == 'happy'
        return False

    def is_angry(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == 'angry'
        return False

    def is_sad(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == 'sad'
        return False

    def want_great_future(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == 'get better'
        return False

    def yes(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == 'yes'
        return False

    def no(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == 'no'
        return False

    def on_enter_rock_song(self, event):
        sender_id = event['sender']['id']
        # responese = send_text_message(sender_id, "Please choose one of the band:\none ok rock\npink noise\nslash")
        
        responese = send_button_message(sender_id, "Please choose one of the band",[{"type":"postback","title":"one ok rock","payload":"one ok rock"},{"type":"postback","title":"pink noise","payload":"pink noise"},{"type":"postback","title":"slash","payload":"slash"}])

    def on_enter_help(self, event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "There are three options:\n1. rock song: to get the rock songs I recommended,\n2. study: song to get some working bgms\n3.talking: get music according to your emotion")
        event['sender']['text']=""
        self.go_back(event)

    def on_enter_ask_emotion(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"How did you feel now?")
        responese = send_button_message(sender_id, "Your feeling",[{"type":"postback","title":"happy","payload":"happy"},{"type":"postback","title":"angry","payload":"angry"},{"type":"postback","title":"sad","payload":"sad"}])
    
    def on_enter_ask_again(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"Now, how did you feel?\nGet better?")
        responese = send_button_message(sender_id, "Your feeling",[{"type":"postback","title":"get better","payload":"get better"},{"type":"postback","title":"angry","payload":"angry"},{"type":"postback","title":"sad","payload":"sad"}])
    
    def on_enter_great_future(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"Now I give you some songs to encourage to improve your life")
        send_video_template(sender_id, "https://www.youtube.com/watch?v=FOvfM0fe-FE&list=PLICIxeiTbvFD_ox665MtNrU8xGjFccRRv")
        send_text_message(sender_id,"Good Bye~~")
        send_attachment_url(sender_id,'image',"https://i.imgur.com/u2xo5S0.jpg")
        self.go_back()


    def on_exit_rock_song(self, event):
        print('Leaving state1')

    def on_enter_one_ok_rock(self, event):
        sender_id = event['sender']['id']
        url=find_song('one ok rock')
        send_video_template(sender_id, url)
        send_text_message(sender_id, "Choose another song: one ok rock\ngo back to rock song: go back")
        event['sender']['text']=""
        self.go_to_again(event)

    def on_enter_pink_noise(self, event):
        sender_id = event['sender']['id']
        send_video_template(sender_id, "https://www.youtube.com/watch?v=PQwYh1bTnUs")
        send_text_message(sender_id, "Choose another song: pink noise\ngo back to rock song: go back")
        event['sender']['text']=""
        self.go_to_again(event)

    def on_enter_slash(self, event):
        sender_id = event['sender']['id']
        url = find_song('slash songs')
        send_video_template(sender_id, url)
        send_text_message(sender_id, "Choose another song: slash\ngo back to rock song: go back")
        event['sender']['text']=""
        self.go_to_again(event)

    def on_enter_study_song(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        
        url = find_song('study music')
        send_video_template(sender_id, url)
        send_text_message(sender_id, "Choose another song: study song\ngo back: return")
        event['sender']['text']=""
        self.go_to_again(event)

    def on_enter_happy(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "That's sound good~ Congratulations\nHere is a song to make you stay in happy")
        url=scrape_song("https://www.youtube.com/playlist?list=PLICIxeiTbvFDIKibqc2cU-zhfX3vxStlU")
        send_video_template(sender_id, url)
        send_button_message(sender_id, "Want another?",[{'type':'postback','title':'Yes','payload':'yes'},{'type':'postback','title':'No','payload':'no'}])
        event['postback']['payload']=""

    def on_enter_angry(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "You must want to roar now\nHere is a song to help you roar")
        url = scrape_song("https://www.youtube.com/playlist?list=PLICIxeiTbvFDqc6aWYdlf8HJVM6gR4ZsK")
        send_video_template(sender_id, url)
        event['postback']['payload']=""
        self.go_to_ask_again(event)


    def on_enter_sad(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "That's too bad\nHere is a song to help you cry")
        url = scrape_song("https://www.youtube.com/playlist?list=PLICIxeiTbvFCGjchFvq4wS7wyAhDw64Db")
        send_video_template(sender_id, url)
        event['postback']['payload']=""
        self.go_to_ask_again(event)

    def on_enter_happy_temp(self,event):
        self.return_happy(event)

