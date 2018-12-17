from transitions.extensions import GraphMachine

from utils import send_text_message, send_attachment_url, send_video_template


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
        

    def is_going_to_rock_song(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'rock song'
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
        return False

    def choose_pink_noise(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'pink noise'
        return False

    def choose_slash(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'slash'
        return False

    def again(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go back'
        return False

    def on_enter_rock_song(self, event):
        # print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "Please choose one of the band:\none ok rock\npink noise\nslash")

    def on_exit_rock_song(self, event):
        print('Leaving state1')

    def on_enter_one_ok_rock(self, event):
        sender_id = event['sender']['id']
        send_video_template(sender_id, "https://www.youtube.com/watch?v=BKz2U4fvA4U&fbclid=IwAR0WxBcfQ37a0AUihNCNKLrsJYYxOPxU330KOQni6p_Fv7u2VRd8Lduz5L8")
        send_text_message(sender_id, "Choose another song: one_ok_rock\ngo back to rock song: go back")

    def on_enter_study_song(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state2")
        send_attachment_url(sender_id, "image", "https://i.imgur.com/5d27rDH.jpg")
        self.go_back()

    def on_exit_study_song(self):
        print('Leaving state2')
