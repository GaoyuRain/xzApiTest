"""
author :admin
Date : 2022/08/15
Description : 告警规则引擎api
"""
import json

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
        params = DataUtils.get_yaml_data('iot_rule_enigne_data', 'create_data_05当前值不等于上一周期的值.yaml')
        print(params)
        r = requests.post(url=url, json=params, cookies=cookie_test, timeout=10)
        print(r.status_code)
        LogUtils.print_response(r)

    @classmethod
    def update(cls):
        url = BASE_RULE_ENIGINE_TEST + '/rule/engine/update'
        # url = BASE_RULE_ENIGINE_TEST + '/rule/engine/update'
        # params = DataUtils.get_yaml_data('iot_rule_enigne_data', 'create_data_07修改参数.yaml')
        params = {"test": "test"}
        # data=json.dumps(params,ensure_ascii=False)
        print(params)
        # print(data)
        r = requests.post(url=url, json=params, cookies=cookie_test, timeout=10)
        print(r.status_code)
        LogUtils.print_response(r)

    @classmethod
    def query(cls):
        # url = BASE_RULE_ENIGINE_TEST + '/rule/engine/queryRuleList'
        url = 'https://iot-rule-engine.dev.ennew.com' + '/rule/engine/queryRuleList'
        # url = BASE_RULE_ENIGINE_TEST + '/rule/engine/update'
        params = {
            "page": 1,
            "pageSize": 10,
            # "ruleId": "",
            # "status": "",
            # "subTenantId": "",
            # "tenantId": ""
        }
        # data=json.dumps(params,ensure_ascii=False)
        print(params)
        # print(data)
        r = requests.post(url=url, json=params, cookies=cookie_test, timeout=10)
        print(r.status_code)
        LogUtils.print_response(r)


if __name__ == '__main__':
    # RuleEnigApi.create()
    RuleEnigApi.update()
    # RuleEnigApi.query()
