"""
author :admin
Date : 2021/11/02
Description :
"""
import json

import requests

from constant import AI_PLATFORM_BASE_URL


class AiPlatformApi:
    HEADER = {
        # 'x-gw-authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjBkeWF3UThlIiwiZXhwIjoxNjM1OTIzMzMwfQ.kNtL_cuNbbeRkIO132j2lgWgjXVpDTzaB8cvtX0evGw',
        'ennunifiedcsrftoken': 'd2882ba7eb45d171dcc698758fbc9865',
        'ennunifiedauthorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJVbmlmeUF1dGhTU08iLCJoYXNUZW5hbnQiOnRydWUsImlzcyI6IjE0MDMyNzMwNTEyMjE4Mzk4NzMiLCJhdWQiOiJhdWQiLCJuYmYiOjE2MzYwNzgxNzEsImFwcElkIjoiYWktcGxhdGZvcm0tc3VwcG9ydCIsIm5pY2tuYW1lIjoi6auY6ZuoIiwidGVuYW50SWQiOiIxMzcxNzUwNDkwNTE3NjYzNzQ1IiwiZ3JhbnRjb2RlIjoiTVRRd016STNNekExTVRJeU1UZ3pPVGczTXlNMVl6QXhZekZsT0RZNE5XSTJNakF5T1dNd1lUUTFPV0ZrWmpnek56QTJZUSIsImV4cCI6MTYzNjE2NDU3MSwiaWF0IjoxNjM2MDc4MTcxLCJqdGkiOiJhZDc3NWNhNS0zMWU0LTQ3ZTEtOTdkNi0xNjk3YWY1YjEyMjEiLCJ1c2VybmFtZSI6InQtR0FPWVVJIn0.CTO2rctnqMPn1ZLXrbPz6HnTu9Wdlkm44L50yC7VYhTMntV-WOwu_cGEmQVstOzT97Xxm8J289am12RoRLLkGf59cHltCuZqFGo7THzGTXrurbHjIHsqQHanULWwGhLQNUbo8RH15FArklBX6krCna8n6c6AjCB0GRk0WU7lA-w'
    }

    @classmethod
    def user_current(cls):
        '''当前用户信息'''
        url = AI_PLATFORM_BASE_URL + '/user/current'
        print(url)
        r = requests.get(url, headers=cls.HEADER)
        print(r.status_code)
        print(r.json())

    @classmethod
    def message_new(cls):
        '''是否有未读新消息'''
        url = AI_PLATFORM_BASE_URL + '/user/message/new'
        print(url)
        r = requests.get(url, headers=cls.HEADER)
        print(r.status_code)
        print(r.json())

    @classmethod
    def content_list(cls):
        '''首页内容列表'''
        url = AI_PLATFORM_BASE_URL + '/content/list'
        print(url)
        r = requests.get(url, headers=cls.HEADER)
        print(r.status_code)
        print(r.json())

    @classmethod
    def user_message(cls):
        '''消息列表'''
        url = AI_PLATFORM_BASE_URL + '/user/message'
        params = {"pageNum": 1, "pageSize": 10}
        r = requests.get(url, params=params, headers=cls.HEADER)
        print(r.status_code)
        print(r.request.url)
        print(r.json())

    @classmethod
    def user_subscribe(cls):
        '''应用订阅信息'''
        url = AI_PLATFORM_BASE_URL + '/subscribe'
        r = requests.get(url, headers=cls.HEADER)
        print(r.status_code)
        print(r.request.url)
        data: dict = r.json()
        print(type(data))
        s = json.loads(data.__str__())
        print(type(s))
        print(data)


if __name__ == '__main__':
    # AiPlatformApi.user_current()
    # AiPlatformApi.message_new()
    # AiPlatformApi.content_list()
    AiPlatformApi.user_message()
    # AiPlatformApi.user_subscribe()
