"""
author :admin
Date : 2021/07/19
Description :
"""
import copy
import json

import ujson

from constant import BASE_DIR


class ParamsUtils:

    @staticmethod
    def get_template_upload_api():
        with open(BASE_DIR + "/datas/template1_coordinate.json", 'r', encoding="utf-8") as f:
            template_coordinate = json.load(f)
            template_coordinate = ujson.load(f)
        with open(BASE_DIR + "/datas/template1_config.json", 'r', encoding="utf-8") as f:
            template_config = json.load(f)
        params = {'formwork_name': 'test报告识别模板1',
                  'type': 'location',
                  'template_coordinate': json.dumps(template_coordinate),
                  'template_config': json.dumps(template_config),
                  'template_method': 'custom',
                  'specific_type': '',
                  'values': ''
                  }
        params1 = copy.deepcopy(params)
        params1.update({'values': '测试正常上传模板功能'})
        params2 = copy.deepcopy(params)
        params2.update({'values': '测试模板名称为空', 'formwork_name': ''})
        params3 = copy.deepcopy(params)
        params3.update({'values': '测试type为空', 'type': ''})
        params4 = copy.deepcopy(params)
        params4.update({'values': '测试type内容错误', 'type': 'htype'})
        params5 = copy.deepcopy(params)
        params5.update({'values': '测试template_coordinate为空', 'template_coordinate': ''})
        params6 = copy.deepcopy(params)
        params6.update({'values': '测试template_config为空', 'template_config': ''})
        params7 = copy.deepcopy(params)
        params7.update({'values': '测试template_config内容错误', 'template_config': '测试内容'})
        params8 = copy.deepcopy(params)
        params8.update({'values': '测试template_method为空', 'template_method': ''})
        params9 = copy.deepcopy(params)
        params9.update({'values': '测试template_method内容错误', 'template_method': '测试内容'})
        return [params1, params2, params3, params4, params5, params6, params7, params8, params9]
