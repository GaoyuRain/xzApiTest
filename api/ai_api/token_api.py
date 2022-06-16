"""
author :admin
Date : 2021/07/16
Description :获取用户token api
"""
import requests

import constant
from utilss.data_utils import DataUtils
from utilss.log_utils import LogUtils


class TokenApi():
    token = '222'

    @classmethod
    def getToken(cls):
        params = {'appId': 'LxwHBR1O', 'appKey': "fc0a677c-08e4-4171-b8ff-9fdf614e4f70", 'appSecret': "M0l5OVVhaW1wdWVOeTZOYVU0RXN2aHBrSDZLRVBySlUzMHduS25jSG80RTZIUWxjV3QybnpNTVNzaHBaU01mNg=="}
        url = "https://middle-open-platform.dev.ennew.com/admin/client/getToken"
        r = requests.get(url, params=params)
        print(r)
        LogUtils.print_response(r)
        # token = {'X-GW-Authorization': r.json().get('datas')}
        # DataUtils.set_data(token, 'user_info.yaml')

    @classmethod
    def test(cls):
        print(cls.token)


if __name__ == '__main__':
    TokenApi.getToken()
    # TokenApi.test()
