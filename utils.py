import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAG2a0mVCxkBAHwSDiL9UQggacpBN5WZBpOegMeEuM4C6096ehWdYeeW5gZBYK6VizqiE2ZAnpYZAgD7cOIiMsbgYSEAE293eZCpVEWMvTMoS0EwZCf6oZCLimK3nzNQZASYdEdSUAd3uIr2HR8J8eTTSqztZCCps5Gh0eWHlT6lxXwZDZD"


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

def send_image_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"attachment": {"type": "image","payload": {"url": text}}}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
