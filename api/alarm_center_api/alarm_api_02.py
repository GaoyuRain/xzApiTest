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
cookie = {"fnw_token": "MTQwMzI3MzA1MTIyMTgzOTg3MyMyQUZDNkYyQS1CN0ZFLTQyNzktOUZCNy1ENTRCMUY1OTI4OEUCLIENT"}


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
        params1 = {"pageIndex": 1, "pageSize": 10, "entId": "1465586144536014850", "openId": "1466418470068551681",
                   "readStatus": None}
        # params1 = {"pageIndex":1,"pageSize":10,"entId":"1291347001673641985","openId":"1468908265805365250","readStatus":None}
        params2 = {"entId": ["1465586144536014850"], "openId": ["1466418470068551681"], "pageNo": 1, "pageSize": 20,
                   "readStatus": [0, 1, 2]}
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

    @classmethod
    def getAlarmHistoryList(cls):
        # url = BASEURL_CONFIG_TEST + '/authenticationFree/inst/getRuleNameList'
        url = BASEURL_CONFIG_TEST + "/authenticationFree/getAlarmHistoryList"
        params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/alram_history_list.json')
        print(type(params))
        data1 = json.dumps(params, ensure_ascii=False)
        data2 = str(json.loads(data1))
        print(data2)

        r = requests.post(url=url, cookies=cookie, json=params, timeout=10)
        LogUtils.print_response(r)

    @classmethod
    def getAlarmHistoryPageForComponent(cls):
        # url = BASEURL_CONFIG_TEST + '/authenticationFree/getAlarmHistoryPageForComponent'
        url = BASEURL_CONFIG_TEST + "/authenticationFree/getAlarmHistoryPageForComponent"
        params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/alram_history_page_component.json')
        print(params)

        r = requests.post(url=url, cookies=cookie, json=params, timeout=10)
        LogUtils.print_response(r)

    @classmethod
    def getAlarmHistorySize(cls):
        # url = BASEURL_CONFIG_TEST + '/authenticationFree/getAlarmHistorySize'
        url = BASEURL_CONFIG_TEST + "/authenticationFree/getAlarmHistorySize"
        params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/alram_history_page_component.json')
        print(params)

        r = requests.post(url=url, cookies=cookie, json=params, timeout=10)
        LogUtils.print_response(r)

    @classmethod
    def getAlarmInfos(cls):
        # url = BASEURL_API_TEST + '/getAlarmInfos'
        url = BASEURL_API_TEST + "/getAlarmInfos"
        params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/get_alarm_infos_data.json')
        print(params)
        r = requests.post(url=url, cookies=cookie, json=params, timeout=10)
        LogUtils.print_response(r)

    @classmethod
    def getAlarmInfosByPage(cls):
        # url = BASEURL_API_TEST + '/getAlarmInfosByPage'
        url = BASEURL_API_TEST + "/getAlarmInfosByPage"
        params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/get_alarm_infos_data.json')
        print(params)
        r = requests.post(url=url, cookies=cookie, json=params, timeout=10)
        LogUtils.print_response(r)

    @classmethod
    def getAlarmInfosFromES(cls):
        # url = BASEURL_API_TEST + '/getAlarmInfosFromES'
        url = BASEURL_API_TEST + "/getAlarmInfosFromES"
        params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/get_alarm_infos_data.json')
        print(params)
        r = requests.post(url=url, cookies=cookie, json=params, timeout=10)
        LogUtils.print_response(r)

    @classmethod
    def getAlarmStatisticByPage(cls):
        # url = BASEURL_API_TEST + '/getAlarmStatisticByPage'
        url = BASEURL_API_TEST + "/getAlarmStatisticByPage"
        params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/get_alarm_infos_data.json')
        print(params)
        r = requests.post(url=url, cookies=cookie, json=params, timeout=10)
        LogUtils.print_response(r)

if __name__ == '__main__':
    # AlarmApi.queryEnum()
    # AlarmApi.getRuleNameList()
    # AlarmApi.getPubAlarmNewHistoryDatas()
    AlarmApi.getAlarmHistoryList()
    # AlarmApi.getAlarmHistoryPageForComponent()
    # AlarmApi.getAlarmHistorySize()
    # AlarmApi.getAlarmInfos()
    # AlarmApi.getAlarmInfosByPage()
    # AlarmApi.getAlarmInfosFromES()
    # AlarmApi.getAlarmStatisticByPage()
    # AlarmApi.getExpParseRules()
    # AlarmApi.updateTagStatus()
