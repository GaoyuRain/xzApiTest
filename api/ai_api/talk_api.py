"""
author :admin
Date : 2021/07/20
Description :
"""
import json

import jwt
import requests
from dill import settings
from jwt import InvalidTokenError

from utilss.log_utils import LogUtils

header = {
    'X-GW-Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6ImhSQ2JDQW5iIiwiZXhwIjoxNjM2NTI1MzgwfQ.s-RTHo-ju5d_r5Y-y60NJGfNn1YtTEFXx-gUkirywBg'}


class TalkApi:

    @staticmethod
    def talk_api():
        url = 'http://open-platform-gateway.dev.ennewi.cn/nlp/chat'
        params = {
            "recipient_id": "zhangzcm",
            "text": "空压系统",
            "scene": "fico"
        }
        r = requests.post(url, json=params, headers=header, timeout=30,
                          verify=False)
        LogUtils.print_response(r)


if __name__ == '__main__':
    TalkApi.talk_api()
    pass
