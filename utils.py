import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAbJkTHym2EBAEAGxZAW0alSu2WRz2fP4hzTKwBEmJzbG0ZC4NRtXHumsaFNyQU5gm7wcXrDWBkc3fp1vHRCB60ZA4CZB4TvGjWyOn8qdsVLhcNZAM2WQjrwKYl3hGG1yR00RmnMTnjiEtjy113CZCvv2MoLGBwvaAvhNHtIXSLszqtdbPnqdt"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


def send_attachment_url(id, attach_type, source_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {
            "attachment":{
                "type":attach_type,
                "payload":{
		    "url":source_url
		}
	    }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_video_template(id, source_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"open_graph",
                    "elements":[
			{
                            "url":source_url
		    	}
		    ]
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response
"""
def send_button_message(id, text, buttons):
    pass
"""
