"""
author :admin
Date : 2021/12/14
Description : 告警api项目
"""
import json

import requests

from utilss.data_utils import DataUtils

# api项目
from utilss.log_utils import LogUtils

BASEURL_API_PROD = "http://alarm-plateform-api.fnwintranet.com"
BASEURL_API_TEST = "http://alarm-plateform-api.test.fnwintranet.com"

# 老告警平台的后端项目
BASEURL_CONFIG_TEST = "http://alarm-config.test.fnwintranet.com"
BASEURL_CONFIG_PROD = "https://dp.fanneng.com/alarmCenter"
cookie = {"fnw_token": "MTQ2MjA1MTQyMzMwOTA2NjI0MiNlMGIyY2MwYmFjYzkxYWZkYTcwZDJiMDc3YWVmOTcwMAPCPC"}


class AlarmApi:

    @classmethod
    def getPubAlarmNewHistoryDatas(cls):
        # 查询所有历史告警消息  pc端和app端
        # {"entId":["1291347001673641985"],"openId":["1516407093500968962"
        # url = 'https://aioper-back.fanneng.com/clickhouse/getPubAlarmNewHistoryDatas'
        url = 'https://aioper-back.fanneng.com//v4/task/getAlarmList'
        # params = {"pageIndex": 180, "pageSize": 10, "status": None}
        # 请求ticket：MjcwNTU0NDAxMDIwMzIwMTUzNiNCQkM1NjE1QS02RUMwLTQwMDAtQTk3MS03Q0EyRUQwRjdDMTUAPP
        # ticket：MTQ2MjA1MTQyMzMwOTA2NjI0MiNBMUVGRTkxMy1FM0Q2LTQ4QTktODEzOS04NTUyOTUyMUI1QjAAPP
        params1 = {"pageIndex":1,"pageSize":10,"entId":"1465586144536014850","openId":"1466418470068551681","readStatus":None}
        # params1 = {"pageIndex":1,"pageSize":10,"entId":"1291347001673641985","openId":"1468908265805365250","readStatus":None}
        params2 = {"entId":["1465586144536014850"],"openId":["1466418470068551681"],"pageNo":1,"pageSize":20,"readStatus":[0,1,2]}
        r = requests.post(url=url, json=params2, timeout=10)
        print(r.status_code)
        print(r.json())

    @classmethod
    def queryEnum(cls):
        url = BASEURL_CONFIG_TEST + '/authenticationFree/label/queryEnum'
        # url = BASEURL_CONFIG_PROD + '/authenticationFree/label/queryEnum'

        r = requests.get(url=url, cookies=cookie, timeout=10)
        print(r.status_code)
        print(r.json())

    @classmethod
    def getRuleNameList(cls):
        # url = BASEURL_CONFIG_TEST + '/authenticationFree/inst/getRuleNameList'
        url = BASEURL_CONFIG_PROD + '/authenticationFree/inst/getRuleNameList'
        params = {
            "entId": "1291347001673641985",
            "pageIndex": 1,
            "pageSize": 10,
            "ruleName": "线上官网入驻企业"
        }
        r = requests.post(url=url, cookies=cookie, json=params, timeout=10)
        print(r.status_code)
        print(r.json())

    @classmethod
    def getExpParseRules(cls):
        url = BASEURL_CONFIG_TEST + '/authenticationFree/inst/getExpParseRules'
        # url = BASEURL_CONFIG_PROD + '/authenticationFree/inst/getExpParseRules'
        params = {"instIds": [961253431483310080]}
        r = requests.post(url=url, cookies=cookie, json=params, timeout=10)
        LogUtils.print_response(r)
        # print(r.status_code)
        # print(r.json())

    @classmethod
    def updateTagStatus(cls):
        # url = BASEURL_CONFIG_TEST + '/authenticationFree/updateTagStatus'
        url = BASEURL_CONFIG_PROD + '/authenticationFree/updateTagStatus'
        params = [{
            "defectTag": 2,
            "ruleId": 1512043117844914176,
            "tagSource": 0,
            "workOrderTag": 2
        }, ]
        r = requests.post(url=url, cookies=cookie, data=params, timeout=10)
        LogUtils.print_response(r)
        print(r.status_code)
        print(r.json())

    # @classmethod
    # def getPubAlarmNewHistoryDatas(cls):
    #     # https://aioper-back.fanneng.com/clickhouse/getPubAlarmNewHistoryDatas
    #     # url = BASEURL_CONFIG_TEST + '/authenticationFree/inst/getRuleNameList'
    #     url = " https://aioper-back.fanneng.com/clickhouse/getPubAlarmNewHistoryDatas"
    #     params = {
    #         "entId": "1437667581924274178",
    #         "pageIndex": 1,
    #         "pageSize": 10,
    #         "ruleName": "线上官网入驻企业"
    #     }
    #     r = requests.post(url=url, cookies=cookie, data=params, timeout=10)
    #     LogUtils.print_response(r)
    #     print(r.status_code)
    #     print(r.json())


if __name__ == '__main__':
    # AlarmApi.queryEnum()
    # AlarmApi.getRuleNameList()
    AlarmApi.getPubAlarmNewHistoryDatas()
    # AlarmApi.getExpParseRules()
    # AlarmApi.updateTagStatus()
