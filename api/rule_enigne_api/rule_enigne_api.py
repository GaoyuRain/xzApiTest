"""
author :admin
Date : 2022/08/15
Description : 告警规则引擎api
"""
import requests

from constant import BASE_RULE_ENIGINE_TEST
from utilss.data_utils import DataUtils
from utilss.log_utils import LogUtils

cookie_test = {"fnw_token": "MTQwMzI3MzA1MTIyMTgzOTg3MyM0OUJFNzMxNC04MzcyLTQ2REUtQTJBNS0zOTQxNkY3RDExQUIPCPC"}


class RuleEnigApi:
    @classmethod
    def create(cls):
        url = BASE_RULE_ENIGINE_TEST + '/rule/engine/create'
        # url = BASE_RULE_ENIGINE_TEST + '/rule/engine/create'
        params = DataUtils.get_yaml_data('iot_rule_enigne_data', 'create_data_01单测点越限.yaml')
        print(params)
        r = requests.post(url=url, json=params, cookies=cookie_test, timeout=10)
        print(r.status_code)
        LogUtils.print_response(r)


if __name__ == '__main__':
    RuleEnigApi.create()
