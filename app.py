import requests
import cv2
import os
import datetime
from argparse import ArgumentParser
from flask import Flask, request, abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# LINE DevelopersのChannel secretとChannel access tokenを入れる
channel_secret = ""
channel_access_token = ""

# directoryの設定
SAVEDIR = ""

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

@app.route("/callback", methods=['POST'])
def callback():    
    signature = request.headers['X-Line-Signature']     
    body = request.get_data(as_text=True)        
    app.logger.info("Request body: " + body)     
    try:         
        handler.handle(body, signature)     
    except InvalidSignatureError:         
        abort(400)
    return 'OK'

# LINEで入力した文字に応じて、動作を決める
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text

    # LINEで撮影と入力するとOK!!!と返信
    # USBカメラで撮影し、LINE Notifyで画像を送信
    if message == "撮影":

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage("OK!!!"))
        
        filename = SAVEDIR + '/face.jpg'
        command = 'fswebcam -r 320x240 -d /dev/video0 ' + filename
        os.system(command)
        os.system('sync')
        
        # 自分のLINE tokenを入れる
        token = ""
        # LINE APIのURL
        url = 'https://notify-api.line.me/api/notify'
        ms_data="image"# メッセージ内容
        
        # message
        send_data = {'message': ms_data}
        # token
        headers = {'Authorization': 'Bearer ' + token}
        # image file
        files = {'imageFile': open(filename, 'rb')}
        #send
        res = requests.post(url, data=send_data, headers=headers, files=files)
        print(res)
    # "撮影"以外のメッセージを入力した場合
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage('"撮影"を入力してください'))


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port ] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8080, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)