"""
author :admin
Date : 2021/07/19
Description :
"""
import json

import requests
from requests import Response

from constant import BASE_DIR
from utilss.log_utils import LogUtils

header = {
    'X-GW-Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6Ik82MWZWTVdpIiwiZXhwIjoxNjI2ODM1MjUwfQ.uaTBU7sIEoItsWX8le1cb8ChJaUoigbsRzQ6h7PkNeM'}


class TemplateRecognizeApi:

    @classmethod
    def upload_pic_api1(cls, params) -> Response:
        url = 'http://open-platform-gateway.dev.ennewi.cn' + "/cv/ocr" + '/template_upload'
        with open(BASE_DIR + '/image/template1.png', 'rb') as f:
            file = {"template_image": ("template1.png", f, 'image/png')}
            r = requests.post(url, data=params, files=file, headers=header, timeout=30,
                              verify=False)
            print(r)
            LogUtils.print_response(r)
        return r

    @classmethod
    def template_recog_api(cls, params) -> Response:
        # 正确 custom-d5581a4f45074128ad8fb7213db42317
        # 错误 custom-e3ddc9a3b03748ac921f97a9cdb7cad5
        url = 'http://open-platform-gateway.dev.ennewi.cn' + "/cv/ocr" + '/template_recog'

        params = {'formwork_id': 'custom-d5581a4f45074128ad8fb7213db42317'}
        with open(BASE_DIR + '/image/template1.png', 'rb') as f:
            file = {"recognition_image": ("template1.png", f, 'image/png')}
            r = requests.post(url, data=params, files=file, headers=header, timeout=30,
                              verify=False)
            print(r)
            LogUtils.print_response(r)
        return r


if __name__ == '__main__':
    with open("../../datas/ai_data/template1_coordinate.json", 'r', encoding="utf-8") as f:
        template_coordinate = json.load(f)
    with open("../../datas/ai_data/template1_config.json", 'r', encoding="utf-8") as f:
        template_config = json.load(f)
    params = {'formwork_name': 'test报告识别模板2',
              'type': 'location',
              'template_coordinate': json.dumps(template_coordinate),
              'template_config': json.dumps(template_config),
              'template_method': 'custom',
              'specific_type': ''}
    # TemplateRecognizeApi.upload_pic_api1(params)
    TemplateRecognizeApi.upload_pic_api1(params={})
