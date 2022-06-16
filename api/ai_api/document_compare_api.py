"""
author :admin
Date : 2021/07/20
Description :
"""
import requests

from constant import AI_BASE_URL, BASE_DIR
from utilss.log_utils import LogUtils

header = {
    'X-GW-Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6Ikx4d0hCUjFPIiwiZXhwIjoxNjM2NTI3NTMwfQ.ncYW5ZzMvyzlAd7PlKYByYzPzgdCysdWjkFvzmdHP1Y'}


class DocumentCompareApi:

    @classmethod
    def document_compare_api(cls):
        url = AI_BASE_URL + '/cv/ocr/document_compare'
        params = {'type': 0, 'callback_interface': ''}
        f1 = open(BASE_DIR + '/datas/ai_data/pngpic1.png', 'rb')
        f2 = open(BASE_DIR + '/datas/ai_data/pngpic2.png', 'rb')
        # file = {"og_file": ("pngpic1.png", f1, 'image/png'),
        #         "ck_file": ("pngpic2.png", f2, 'image/png') }

        file = {'og_file': f1, 'ck_file': f2}
        r = requests.post(url, data=params, files=file, headers=header, timeout=50, verify=False)
        print(r)
        LogUtils.print_response(r)
        f1.close()
        f2.close()

    @classmethod
    def compare_result_api(cls):
        # "diff_id": "036d0b778cff45b0b15974887f22708c"
        pass


if __name__ == '__main__':
    DocumentCompareApi.document_compare_api()
