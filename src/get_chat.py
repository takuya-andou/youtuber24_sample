import httplib2
import httplib2
from oauth2client import tools
from oauth2client import client
from oauth2client.file import Storage
import json
import time
from conversation import postConv

youtubeURL = 'https://youtu.be/*********'


def urlGet():
    print("取得したyoutubeliveID：" + youtubeURL[-11:])
    urlP = youtubeURL[-11:]

    credentials_path = "./cred.json"
    store = Storage(credentials_path)
    credentials = store.get()

    if credentials is None or credentials.invalid:
        f = "./client.json"
        scope = "https://www.googleapis.com/auth/youtube.readonly"
        flow = client.flow_from_clientsecrets(f, scope)
        flow.user_agent = "APIキー"
        credentials = tools.run_flow(flow, Storage(credentials_path))

    http = credentials.authorize(httplib2.Http())
    url = "https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id="
    url += urlP

    res, data = http.request(url)
    data = json.loads(data.decode())
    print(data)
    try:
        chat_id = data["items"][0]["liveStreamingDetails"]["activeLiveChatId"]
    except:
        print("生放送読み込みエラー")
        return

    print("チャットID：" + chat_id)
    print("チャットID取得")

    url = "https://www.googleapis.com/youtube/v3/liveChat/messages?part=snippet,authorDetails"
    url += "&liveChatId=" + chat_id

    commentGet(data, url, http)


def commentGet(data, url, http):
    commentDifference = ""
    commentDBlue = False

    print("コメント取得開始")
    while True:
        res, data = http.request(url)
        data = json.loads(data.decode())

        if data.get("items"):  # 取得できなかった場合のため
            for datum in data["items"]:
                snippet = datum.get("snippet")
                if snippet.get("textMessageDetails"):
                    textMessageDetails = snippet.get("textMessageDetails")
                    if textMessageDetails.get("messageText"):

                        comment = datum["snippet"][
                            "textMessageDetails"]["messageText"]
                        name = datum["authorDetails"]["displayName"]

                        if commentDBlue == True:
                            print(name + ": " + comment)
                            print(postConv(comment))

                        if commentDifference == name + ":" + comment:
                            commentDBlue = True

                        commentDifference_middle = name + ":" + comment

        commentDifference = commentDifference_middle
        time.sleep(0.5)
        commentDBlue = False

if __name__ == '__main__':
    urlGet()
