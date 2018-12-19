import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAG2a0mVCxkBAPqSaS2QZCPGRHu5hqyDnXlZAiFrB6gJ8ndi0fye64C5ma4x6LPhTxIAPLG9a21kZAJZAHYuU07N8nlZANzV8lBHEZAkIyZBaeNDqaQbaEuoqZAepkVLj2wEj5BPKXKw70YilH1tUZCHktPriwvU7aZAh4wtULxAFdYQZDZD"


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


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
