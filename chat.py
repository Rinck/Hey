#!/usr/bin/env python
# coding:utf-8


import json
import urllib.request



RATE = "16000"
FORMAT = "wav"
CUID = "wate_play"
DEV_PID = "1536"

framerate = 16000
NUM_SAMPLES = 2000
channels = 1
sampwidth = 2
TIME = 2

def answer(mytext):
    api_url = "http://openapi.tuling123.com/openapi/api/v2"
    req = {
        "perception":
        {
            "inputText":
            {
                    "text": mytext
            },

            "selfInfo":
            {
                "location":
                    {
                        "city": "东莞",
                        "province": "广东",
                         "street": "建新路"
                    }
            }
        },

        "userInfo":
        {
            "apiKey": "bd67fa03a12340be8c68d502640cd369",
            "userId": "350492"
        }
    }

    # print(req)
    # 将字典格式的req编码为utf8
    req = json.dumps(req).encode('utf8')
    # print(req)

    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    # print(response_str)
    response_dic = json.loads(response_str)
    # print(response_dic)

    intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']
    print('小霖：' + results_text)
    return results_text
