#!/usr/bin/env python
# coding:utf-8

from aip import AipSpeech
import base64
import json
import os
import requests


# 获取你的token
def get_token():
    server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    # API Key
    client_id = "您的百度云 API Key"
    # Secret Key
    client_secret = "您的百度云的Secret Key"

    # 拼url
    url = "%sgrant_type=%s&client_id=%s&client_secret=%s" % (server, grant_type, client_id, client_secret)
    # 获取token
    res = requests.post(url)
    token = json.loads(res.text)["access_token"]
    return token 


RATE = "16000"
FORMAT = "wav"
CUID = "wate_play"
DEV_PID = "1536"


# 把语音转换成文字
def get_word(token):
    with open(r'01.wav', "rb") as f:
        speech = base64.b64encode(f.read()).decode('utf8')
    size = os.path.getsize(r'01.wav')
    headers = {'Content-Type': 'application/json'}
    url = "https://vop.baidu.com/server_api"
    data = {
        "format": FORMAT,
        "rate": RATE,
        "dev_pid": DEV_PID,
        "speech": speech,
        "cuid": CUID,
        "len": size,
        "channel": 1,
        "token": token,
    }

    req = requests.post(url, json.dumps(data), headers)
    result = json.loads(req.text)
    ret = result["result"][0]
    return ret



#把文字转换成语音
def toVioce(voiceanserver):
    APP_ID = '14846238'
    API_KEY = 'X6uxcsmsWKqn8r2c1BIvYmHc'
    SECRET_KEY = 'L3SbGwk5TKf0Gmnupz6iSgUVOg93TzQy'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result = client.synthesis(voiceanserver, 'zh', 1, {
        'vol': 5, 'per': 4,
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)