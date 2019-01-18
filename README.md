# youtuber24_sample
24時間生放送をし続けるyoutuberのサンプル

https://blog.takuya-andou.com/entry/24_youtuber_2

# 注意
このソースだとYoutubeDataAPIの1日の制限数を超えてしまうため、30分程度しか耐えられませんでした。

# 実行方法
## 初回のみ
- [GCP](https://console.cloud.google.com/)でプロジェクト作成やAPIの有効化をしておく（[ここ](https://blog.sky-net.pw/article/86)を参考にした）
- `src/` のoauth2.pyを実行し、鍵ファイルを生成。 `src/` の下に配置。
- [TALK API](https://a3rt.recruit-tech.co.jp/product/talkAPI/)のAPI KEYを発行
- `docker-compose.yml`内のAPI KEYを書き換え

## コンテナを落とすたびに実行が必要なもの
- `docker-com pose up -d`
- `docker exec -it youtuber24 ash`
- `pip install -r requirements.txt`

## 毎回
- `src/get_chat.py`内のyoutubeURLを書き換え
- `python get_chat.py`


# 参考にしたページ
[Youtube LiveStreaming APIで配信のコメントを取得する](https://blog.sky-net.pw/article/86)  
[【 メモ 】YoutubeLiveのコメント取得 ( Python )](http://blog.livedoor.jp/engineersoku/9957130.html)
