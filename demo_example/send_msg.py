import os
import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = os.environ.get("EAAbJkTHym2EBALQKye88hzOgZA0siavGKlkuEmgHLmOO6t8gV3QRsfOObSIunifGFiZCYQVr9cs7UKDQQ9deyizOUi19oNcZB9DVOE5ZAFl0muBLnnqrGQ7uqjVDYbbNdBiWEmSF0ycWLKZC7hiRTIKZCgZAZCxncTSwJ3XX5ziZBV1treZBLmBPQz")


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response.text
