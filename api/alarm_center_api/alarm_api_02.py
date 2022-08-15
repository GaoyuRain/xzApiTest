"""
author :admin
Date : 2021/12/14
Description : 告警api项目
"""
import json

import requests

from constant import BASE_ALARM_CON_URL, BASE_ALARM_API_URL
from utilss.data_utils import DataUtils

# api项目
from utilss.log_utils import LogUtils

BASEURL_API_PROD = "http://alarm-plateform-api.fnwintranet.com"
BASEURL_API_TEST = "http://alarm-plateform-api.test.fnwintranet.com"

# 老告警平台的后端项目
BASEURL_CONFIG_TEST = "http://alarm-config.test.fnwintranet.com"
BASEURL_CONFIG_PROD = "https://dp.fanneng.com/alarmCenter"
cookie_test = {"fnw_token": "MTQwMzI3MzA1MTIyMTgzOTg3MyM0OUJFNzMxNC04MzcyLTQ2REUtQTJBNS0zOTQxNkY3RDExQUIPCPC"}
cookie_prod = {"fnw_token": "MTQ2MjA1MTQyMzMwOTA2NjI0MiMxMkI3MTlGRi0xRkZGLTRCNzUtQjExNi00MzM5QjgzRjY3NTgPCPC"}


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

        r = requests.get(url=url, cookies=cookie_test, timeout=10)
        print(r.status_code)
        print(r.json())

    @classmethod
    def getAlarmInstanceInfoPage(cls):
        url = BASEURL_CONFIG_TEST + '/GroupingAndRuleTemplates/getAlarmInstanceInfoPage'
        # url = BASEURL_CONFIG_PROD + '/alarmCenter/GroupingAndRuleTemplates/getAlarmInstanceInfoPage'
        params={"pageIndex":1,"pageSize":10,"name":"",
                "entId":"1367677007133487106","ruleStatus":[],
                "alarmMainLevel":[],"alarmTags":[],"notifyFlag":[],
                "type":"1","mouldId":"","equipParentType":"","equipSonType":""}
        r = requests.post(url=url, cookies=cookie_test, json=params, timeout=10)
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
        r = requests.post(url=url, cookies=cookie_test, json=params, timeout=10)
        print(r.status_code)
        print(r.json())

    @classmethod
    def getExpParseRules(cls):
        url = BASEURL_CONFIG_TEST + '/authenticationFree/inst/getExpParseRules'
        # url = BASEURL_CONFIG_PROD + '/authenticationFree/inst/getExpParseRules'
        params = {"instIds": [961253431483310080]}
        r = requests.post(url=url, cookies=cookie_test, json=params, timeout=10)
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
        r = requests.post(url=url, cookies=cookie_test, data=params, timeout=10)
        LogUtils.print_response(r)
        print(r.status_code)
        print(r.json())

    @classmethod
    def getAlarmHistoryList(cls):
        # 查询告警历史信息--以事件为主
        url = BASE_ALARM_CON_URL + "/authenticationFree/getAlarmHistoryList"
        params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/alram_history_list.json')
        # params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/alram_history_list_prod.json')
        print(type(params))
        data1 = json.dumps(params, ensure_ascii=False)
        data2 = str(json.loads(data1))
        print(data2)

        r = requests.post(url=url, cookies=cookie_prod, json=params, timeout=10)
        LogUtils.print_response(r)


    @classmethod
    def getAlarmHistoryPageForComponent(cls):
        # 报警历史分页--统一运维工作台
        url = BASE_ALARM_CON_URL + '/authenticationFree/getAlarmHistoryPageForComponent'
        # params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/alram_history_page_component.json')
        params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/alram_history_page_component_prod.json')
        print(params)

        r = requests.post(url=url, cookies=cookie_test, json=params, timeout=10)
        LogUtils.print_response(r)

    @classmethod
    def getAlarmHistorySize(cls):
        url = BASE_ALARM_CON_URL + '/authenticationFree/getAlarmHistorySize'
        # params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/alram_history_page_component.json')
        params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/alram_history_page_component_prod.json')
        print(params)

        r = requests.post(url=url, cookies=cookie_test, json=params, timeout=10)
        LogUtils.print_response(r)

    @classmethod
    def getAlarmInfos(cls):
        url = BASE_ALARM_API_URL + '/getAlarmInfos'
        # params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/get_alarm_infos_data.json')
        params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/get_alarm_infos_data_prod.json')
        print(params)
        r = requests.post(url=url, cookies=cookie_test, json=params, timeout=10)
        LogUtils.print_response(r)

    @classmethod
    def getAlarmInfosByPage(cls):
        url = BASE_ALARM_API_URL + '/getAlarmInfosByPage'
        # params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/get_alarm_infos_bypage_fes.json')
        params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/get_alarm_infos_bypage_fes_prod.json')
        print(params)
        r = requests.post(url=url, cookies=cookie_test, json=params, timeout=10)
        LogUtils.print_response(r,isformart=True)

    @classmethod
    def getAlarmInfosFromES(cls):
        url = BASE_ALARM_API_URL + '/getAlarmInfosFromES'
        # params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/get_alarm_infos_bypage_fes.json')
        params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/get_alarm_infos_bypage_fes_prod.json')
        print(params)
        r = requests.post(url=url, cookies=cookie_test, json=params, timeout=10)
        LogUtils.print_response(r)

    @classmethod
    def getAlarmStatisticByPage(cls):
        url = BASE_ALARM_API_URL + "/getAlarmStatisticByPage"
        params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/get_alarm_infos_data.json')
        print(params)
        r = requests.post(url=url, cookies=cookie_test, json=params, timeout=10)
        LogUtils.print_response(r)

if __name__ == '__main__':
    # AlarmApi.queryEnum()
    # AlarmApi.getAlarmInstanceInfoPage()
    # AlarmApi.getRuleNameList()
    # AlarmApi.getPubAlarmNewHistoryDatas()
    AlarmApi.getAlarmHistoryList()
    # AlarmApi.getAlarmHistoryPageForComponent()
    # AlarmApi.getAlarmHistorySize()
    # AlarmApi.getAlarmInfosByPage()
    # AlarmApi.getAlarmInfosFromES()
    # AlarmApi.getAlarmInfos()
    # AlarmApi.getAlarmStatisticByPage()
    # AlarmApi.getExpParseRules()
    # AlarmApi.updateTagStatus()
