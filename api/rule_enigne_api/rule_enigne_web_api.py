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
    def getAlarmHistoryList(cls):
        url = 'https://iot-alarm-web.dev.ennew.com' + '/alarm/getAlarmHistoryList'
        # url = BASE_RULE_ENIGINE_TEST + '/rule/engine/create'
        # , "ruleId": "1578926408111783936"
        params = {"page": 1, "pageSize": 10, "productId": "1567007800812236802", "startTime": "2022-10-09 09:56:56",
                  "endTime": "2022-10-09 10:02:52", "ruleId": "1578926408111783936"}
        print(params)
        r = requests.post(url=url, json=params, cookies=cookie_test, timeout=10)
        print(r.status_code)
        LogUtils.print_response(r)


if __name__ == '__main__':
    RuleEnigApi.getAlarmHistoryList()
