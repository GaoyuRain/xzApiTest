"""
author :rain
Date : 2020/10/27
Description :
"""
import requests

import constant
from utilss.data_utils import DataUtils
from utilss.log_utils import LogUtils


class APIUtils:

    @staticmethod
    def send_req(type, url, params):
        '''调试用'''
        type = type.lower()
        # header = DataUtils.get_user_info_auto()

        requests.DEFAULT_RETRIES = 5
        s = requests.session()
        s.keep_alive = False
        if 'get'.__eq__(type):
            r = requests.get(url, headers=constant.HEADER, params=params, timeout=10)
        else:
            r = requests.post(url, headers=constant.HEADER, json=params, timeout=10)
        LogUtils.print_response(r, isformart=True)
        return r
