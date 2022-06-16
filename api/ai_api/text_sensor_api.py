"""
author :admin
Date : 2021/07/23
Description : 文本审核
"""
from constant import HEADER, AI_BASE_URL
from utilss.api_utils import APIUtils


class TextSensorApi:
    @classmethod
    def text_sensor(cls):
        url = AI_BASE_URL + '/nlp/text_censor'
        header = HEADER
        params = {"text": "nihao", "scene": 0, "user_id": "1403273051221839873"}
        APIUtils.send_req('post', url, params)


if __name__ == '__main__':
    TextSensorApi.text_sensor()
