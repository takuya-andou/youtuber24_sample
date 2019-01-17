import requests
import json
import time
import os

def postConv(conv_contents):
    files = {
        'apikey': (None, os.environ["apikey"]),
        'query': (None, conv_contents),
    }

    r = requests.post(
        'https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk',  files=files)
    res = json.loads(r.text)
    try:
        reply = res["results"][0]["reply"]
        return reply
    except:
        return "404"
