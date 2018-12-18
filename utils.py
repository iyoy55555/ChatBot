import re
import requests
import random
from bs4 import BeautifulSoup

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

def find_song(key_word):
    list1 = []
    count=0
    last = None
    url="https://www.youtube.com/results?search_query="+key_word
    res = requests.get(url,verify = False)
    soup=BeautifulSoup(res.text,'html.parser')
    for entry in soup.select('a'):
        m=re.search("v=(.*)",entry['href'])
        if m:
            if last == m.group(1):
                continue
            if re.search("list",m.group(1)):
                continue
            last = m.group(1)
            list1.append('https://www.youtube.com/watch?v='+m.group(1))
    return list1[random.randint(0,len(list1)-1)]

def scrape_song(url):
    list1 = []
    count=0
    last = None
    res = requests.get(url,verify = False)
    soup=BeautifulSoup(res.text,'html.parser')
    for entry in soup.select('a'):
        m=re.search("v=(.*)",entry['href'])
        if m:
            if last == m.group(1):
                continue
            last = m.group(1)
            list1.append('https://www.youtube.com/watch?v='+m.group(1))
    return list1[random.randint(0,len(list1)-1)]

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


def send_button_message(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"generic",
                    "elements":[
			{
                            "title":text,
                            "buttons":buttons
		    	}
		    ]
                }
            }
        }
    }
    response = requests.post(url, json=payload)


