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
BASEURL_CONFIG_TEST = "http://alarm-config.test.fnwintranet.com"

# 老告警平台的后端项目
BASEURL_CONFIG_PROD = "https://dp.fanneng.com/alarmCenter"
cookie = {"fnw_token": "ODEzNTA5OTc1ODU1MDM4NDY0MCMwMzcyRDI5Ni1BRjQ4LTREMUItQkY1OS1DMEJEQkJEOTM5MUECLIENT"}


class AlarmApi:

    @classmethod
    def inst_jumpMouldCreateRule(cls):
        # 跳过模板直接生成规则
        # url = BASEURL_CONFIG_PROD + '/inst/jumpMouldCreateRule'
        url = BASEURL_API_TEST + '/inst/jumpMouldCreateRule'
        # url = BASEURL_API_PROD + '/inst/jumpMouldCreateRule'
        params = DataUtils.get_json_data('alarm_center_api_data', 'fn_跳过模板创建规则01.json')
        # params = DataUtils.get_json_data('alarm_center_api_data', 'fn_跳过模板创建规则01_prod_新.json')
        # r = requests.post(url, json=params, timeout=30)
        r = requests.post(url, json=params, timeout=30, cookies=cookie)
        print(r.status_code)
        print(r.json())

    @classmethod
    def inst_jumpMouldCreateRuleSimple(cls):
        # 跳过模板直接生成规则 不包含触达
        url = BASEURL_API_PROD + '/inst/jumpMouldCreateRuleSimple'
        params = DataUtils.get_json_data('alarm_center_api_data', 'fn_跳过模板创建规则不包含触达01_prod.json')
        r = requests.post(url, json=params, timeout=10)
        print(r.status_code)
        print(r.json())

    @classmethod
    def inst_forbiddenByMouldIds(cls):
        # 根据模板id 启用/禁用告警实例规则   1 启用  0 禁用
        url = BASEURL_API_TEST + '/inst/forbiddenByMouldIds'
        # url = BASEURL_API_PROD + '/inst/forbiddenByMouldIds'
        data = {'MouldIds': '942721739268538368', 'status': '1'}
        r = requests.post(url, data=data, timeout=10)
        print(r.status_code)
        print(r.json())

    @classmethod
    def groupingAndRuleTemplates_startingOrForbidden(cls):
        # 根据规则id 启用/禁用告警实例规则   1 启用  0 禁用
        url = BASEURL_CONFIG_TEST + '/GroupingAndRuleTemplates/startingOrForbidden'
        url = BASEURL_API_TEST + '/GroupingAndRuleTemplates/startingOrForbidden'
        # url = BASEURL_API_PROD + '/GroupingAndRuleTemplates/startingOrForbidden'
        # params = {"id": [999318166888525824], "status": "1"}
        params = ["20220720141344551436965799989285","0"]
        r = requests.post(url, json=params, timeout=10, cookies=cookie)
        print(r.status_code)
        print(r.json())

    @classmethod
    def inst_updateExpression(cls):
        # 修改表达式
        url = BASEURL_API_TEST + '/inst/updateExpression'
        params = DataUtils.get_json_data('alarm_center_api_data', 'fn_api修改表达式01.json')
        r = requests.post(url, json=params, timeout=10)
        print(r.status_code)
        print(r.json())

    @classmethod
    def groupingAndRuleTemplates_deletedAlarmInstanceInfo(cls):
        # 根据规则id 删除规则
        # 946469238842023936 2022-02-24 18:10:52
        # 946487488598683648 2022-02-24 19:24:34O
        url = BASEURL_API_PROD + '/GroupingAndRuleTemplates/deletedAlarmInstanceInfo'
        params = {"id": [946469238842023936, 946487488598683648], "status": ""}
        r = requests.post(url, json=params, timeout=10)
        print(r.status_code)
        print(r.json())

    @classmethod
    def groupingAndRuleTemplates_getAlarmHistoryPageByInstanceId(cls):
        # 报警历史分页
        url = BASEURL_API_PROD + '/GroupingAndRuleTemplates/getAlarmHistoryPageByInstanceId'
        params = {"endTime": "", "startTime": "",
                  # 线上
                  "entId": "1291347001673641985",
                  "instanceId": 946469238842023936,
                  # 测试
                  # "entId": "1254591591796961281",
                  # "instanceId": 919978786482716672,
                  "pageIndex": 1,
                  "pageSize": 20,
                  "sTriggerTime": "2022-02-13",
                  "eTriggerTime": "2022-03-01"}

        r = requests.post(url, json=params, timeout=10)
        print(r.status_code)
        print(r.json())

    @staticmethod
    def get_history_by_date_and():
        url = BASEURL_CONFIG_PROD + "/GroupingAndRuleTemplates/getAlarmHistoryPageByInstanceIdAndDate"
        print(url)
        # params = {"sTriggerTime": "2022-03-03 18:37:54",
        #           "eTriggerTime": "2022-03-08 19:17:54",
        #           "equipIds": ["METE_METE01"],
        #           # "instanceId": "949020079325667328",
        #           "pageIndex": 1, "pageSize": 10,
        #           "entId": "1291347001673641985",
        #           "equipName": "线上官网入驻企业流程测试/一食堂-14#0.4kV进线-映射",
        #           }

        params = {"sTriggerTime": "2022-05-15 22:28:45", "eTriggerTime": "2022-05-15 22:49:43",
                  "instanceId": "964854554735525894", "pageIndex": 1, "pageSize": 10, "entId": "1367778980448231426",
                  "equipName": "成品板栗库DTU", "eventId": "1641439"}

        # "eventId": "231266905"
        r = requests.post(url, json=params, timeout=240, cookies=cookie)
        print(r)
        print(r.status_code)
        # print(r.text)
        print(r.json())

    @classmethod
    def groupingAndRuleTemplates_getAlarmHistoryPageByInstanceIdAndDate(cls):
        # 通过时间报警历史分页
        # url = BASEURL_API_TEST + '/GroupingAndRuleTemplates/getAlarmHistoryPageByInstanceIdAndDate'
        url = BASEURL_API_PROD + '/GroupingAndRuleTemplates/getAlarmHistoryPageByInstanceIdAndDate'
        # url = BASEURL_CONFIG_PROD + '/GroupingAndRuleTemplates/getAlarmHistoryPageByInstanceIdAndDate'
        params = {"sTriggerTime": "2022-02-03  13:41:08",
                  "eTriggerTime": "2022-03-16  13:41:08",
                  "equipIds": ["METE_METE01"],
                  # 线上
                  "entId": "1291347001673641985",
                  "instanceId": 920394864678039552,
                  # 测试
                  # "entId": "1254591591796961281",
                  # "instanceId": 923597006184189952,
                  "pageIndex": 1,
                  "pageSize": 20}

        r = requests.post(url, json=params, timeout=50)
        LogUtils.print_response(r)
        print(r.status_code)
        print(r.json())

        # /inst/getRulesBatch

    @classmethod
    def getRulesBatch(cls):
        #
        url = BASEURL_CONFIG_PROD + '/inst/getRulesBatch'
        params = {
            "instIds": ["874672492795011072"]
        }
        r = requests.post(url, json=params, cookies=cookie, timeout=10)
        LogUtils.print_response(r)

    @classmethod
    def alarmplatformjurisdiction_save(cls):
        # 增加管理员权限

        url = BASEURL_CONFIG_TEST + '/alarmplatformjurisdiction/save'
        # url = BASEURL_CONFIG_PROD + '/alarmplatformjurisdiction/save'
        params = {
            "createTime": "",
            "creator": "高雨",
            # 生产
            # "entId": "1291347001673641985",
            # "openId": "1468908265805365250",
            # 测试
            "entId": "1513729414538637313",
            "openId": "1464525590919553026",
            # "id": 0,
            # "isDel": 0,
            "name": "张锁锋",
            "update_time": "",
            "updator": "高雨"
        }
        r = requests.post(url=url, cookies=cookie, json=params, timeout=10)
        print(r.status_code)
        print(r.json())

    #

    @classmethod
    def resultAndEvent_updateEventRecoverStatus(cls):
        # url = BASEURL_CONFIG_TEST + '/ResultAndEvent/updateEventRecoverStatus'
        url = BASEURL_CONFIG_PROD + '/ResultAndEvent/updateEventRecoverStatus'
        list = {[{"alarmId": 276382118,
                  "ruleId": 959185003742978048}]}
        params = json.dumps(list)
        print(params)

        r = requests.post(url=url, cookies=cookie, json=params, timeout=10)
        print(r.status_code)
        print(r.json())


if __name__ == '__main__':
    # 跳过模板直接生成规则 111
    AlarmApi.inst_jumpMouldCreateRule()
    # 根据规则id 启用/禁用告警实例规则 111
    # AlarmApi.groupingAndRuleTemplates_startingOrForbidden()
    # 跳过模板直接生成规则 不包含触达 111
    # AlarmApi.inst_jumpMouldCreateRuleSimple()
    # 修改表达式 111
    # AlarmApi.inst_updateExpression()
    # 根据模板id 启用/禁用告警实例规则 1111
    # AlarmApi.inst_forbiddenByMouldIds()
    # 报警历史分页 111
    # AlarmApi.groupingAndRuleTemplates_getAlarmHistoryPageByInstanceId()
    # 通过时间报警历史分页 111
    # AlarmApi.groupingAndRuleTemplates_getAlarmHistoryPageByInstanceIdAndDate()
    # 根据规则id 删除规则 111
    # AlarmApi.groupingAndRuleTemplates_deletedAlarmInstanceInfo()
    # 报警历史分页 111
    # 通过时间报警历史分页 111
    # AlarmApi.get_history_by_date_and()
    # AlarmApi.getRulesBatch()
    # AlarmApi.alarmplatformjurisdiction_save()
    # AlarmApi.resultAndEvent_updateEventRecoverStatus()
