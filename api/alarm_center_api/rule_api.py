"""
author :admin
Date : 2021/09/13
Description :
"""
import requests

from constant import ALARM_CENTER_URL_DEV, ALARM_CENTER_URL_prod
from utilss.data_utils import DataUtils

apiauth_header = {"ennunifiedcsrftoken": "3f210aa54d59c513aeeb99e44c69e60d",
                  "ennunifiedauthorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJVbmlmeUF1dGhTU08iLCJoYXNUZW5hbnQiOnRydWUsImlzcyI6IjE0MDMyNzMwNTEyMjE4Mzk4NzMiLCJ0ZXJtaW5hbFR5cGUiOiJQQy1XRUIiLCJhdWQiOiJhdWQiLCJuYmYiOjE2NDMzMzQzOTMsImFwcElkIjoiYWxhcm0tY2VudGVyIiwibmlja25hbWUiOiLpq5jpm6giLCJ0ZW5hbnRJZCI6IjEzNjk1NTk5NzAyMjE5ODU3OTQiLCJncmFudGNvZGUiOiJNVFF3TXpJM016QTFNVEl5TVRnek9UZzNNeU5oTWpOaU5tWXlZVGs1WlROak1qSTVZVEJpTmpaa1lUVXhNVGcwT1RJME9RIiwiZXhwIjoxNjQzNDIwNzkzLCJpYXQiOjE2NDMzMzQzOTMsImp0aSI6ImU1ZTM4N2VlLTg0ZmUtNDI5Mi1iOWQ2LWFlMTVkYTRkMGJiMCIsInVzZXJuYW1lIjoidC1HQU9ZVUkifQ.70YQZfVYjEeu6d3Kz61Zh7LYh8-OjWQwKmZGM9tb0-qjep-PLBOTH0jTldWjUDdL_zio8V-zMDsxJvMLodVlWoo4N5N0zz3WoWnsDxrhsdLshdphS2kxmpPT1q8bn6olcyD4jMCDBHSaK0a51ux-Ma0J2bZm_3rfkidSOmcWoD0"}


class RuleApi:

    @staticmethod
    def create_rule():
        # url = ALARM_BASER_URL_DEV + "/alarmRule/createRule"
        # url = ALARM_BASER_URL_prod + "/alarmRule/createRule"
        url = ALARM_CENTER_URL_DEV + "/alarmRule/createRule"
        print(url)
        header = {"accessToken": "APM"}
        header = {"accessToken": "fanNeng"}
        params = DataUtils.get_json_data('alarm_center_api_data', 'rule_自动恢复_单测点阈值越限.json')
        # params = DataUtils.json_to_yaml('alarm_center_api_data', 'rule_apm告警转工单时间升级PROD.json')
        # r = requests.post(url, json=params, headers=apiauth_header, timeout=10)
        r = requests.post(url, headers=header, json=params, timeout=20)
        print(r.status_code)
        print(r.json())

    @staticmethod
    def create_simple_rule():
        url = ALARM_CENTER_URL_DEV + "/alarmRule/createOrUpdateRuleSimple"
        print(url)
        header = {"accessToken": "fanNeng"}
        params = DataUtils.get_json_data('alarm_center_api_data', '自动恢复_简易配置规则A越限.json')
        print(params)
        r = requests.post(url, json=params, headers=header, timeout=10)
        print(r.status_code)
        print(r.json())

    @staticmethod
    def create_update_status():
        url = ALARM_CENTER_URL_DEV + "/alarmRule/updateStatus"
        print(url)
        header = {"accessToken": "fanNeng"}
        params = {
            "ruleIds": [1482985906373902336],
            "ruleType": 0,
            "status": 0,
            "tenantId": "fanNeng"
        }
        print(params)
        r = requests.post(url, json=params, headers=header, timeout=10)
        print(r.status_code)
        print(r.json())

    @staticmethod
    def update_rule():
        url = ALARM_CENTER_URL_DEV + "/alarmRule/createRule"
        params = DataUtils.get_json_data('alarm_center_api_data', '')
        r = requests.post(url, json=params, timeout=10)
        print(r.status_code)
        print(r.json())

    @staticmethod
    def trigger_event():
        url = ALARM_CENTER_URL_DEV + '/alarmEvent/triggerEvent'
        params = {"eventId": 1453178185765523458, "eventName": "test016告警动作05", "ruleId": 1453178184941047808}
        r = requests.post(url, json=params, timeout=10)
        print(r.status_code)
        print(r.json())

    @staticmethod
    def query_rule():
        url = ALARM_CENTER_URL_DEV + '/alarmRule/queryRule'
        params = {'ruleId': '1449979087065059328'}
        r = requests.get(url, params=params)
        print(r.status_code)
        print(r.json())

    @staticmethod
    def query_event():
        url = ALARM_CENTER_URL_DEV + '/alarmEvent/listEvent'
        params = {'ruleId': '1442063255148302336'}
        r = requests.get(url, params=params)
        print(r.status_code)
        print(r.json())

    @staticmethod
    def query_alarm_record_list():
        url = ALARM_CENTER_URL_DEV + '/alarmRecord/list'
        params = {"ruleIds": [1450373590758330368], "starDate": "2021-10-20 10:13:00",
                  "endDate": "2021-10-20 19:13:00", "page": 1, "pageSize": 20}
        r = requests.post(url, json=params, timeout=10)
        print(r.status_code)
        print(r.json())

    @staticmethod
    def query_all_alarm_record_list():
        url = ALARM_CENTER_URL_DEV + '/alarmRecord/listAll'
        params = {"ruleIds": [1450373590758330368], "starDate": "2021-10-20 10:13:00",
                  "endDate": "2021-10-20 19:13:00", "page": 1, "pageSize": 20}
        r = requests.post(url, json=params, timeout=10)
        print(r.status_code)
        print(r.json())

    @staticmethod
    def creat_fb_work_by_user():
        '''手动创建工单'''
        url = ALARM_CENTER_URL_DEV + "/ruleAlarm/createFbWorkByUser"
        params = {"alarmId": 377748}
        r = requests.post(url, json=params, timeout=10)
        print(r.status_code)
        print(r.json())

    @staticmethod
    def close_fb_work_by_user():
        '''关闭工单-测试用'''
        url = ALARM_CENTER_URL_DEV + '/ruleAlarm/closeFbWorkByUser'
        params = {"alarmId": 365984}
        r = requests.post(url, json=params, timeout=10)
        print(r.status_code)
        print(r.json())



    @staticmethod
    def delete_rule():
        url = ALARM_CENTER_URL_DEV + '/alarmRule/deleteRule'
        # url = ALARM_BASER_URL_prod + '/alarmRule/deleteRule'
        header = {"accessToken": "fanNeng"}
        # 1496102157065273344
        params = {'ruleId': '1509799288480407552'}
        r = requests.get(url, headers=header, params=params)
        print(r.status_code)
        print(r.json())



if __name__ == '__main__':
    # ai-platform-support ; enn-sim-sys-service ;
    # RuleApi.create_rule()
    # RuleApi.create_simple_rule()
    # RuleApi.update_rule()
    # RuleApi.create_update_status()
    # RuleApi.trigger_event()
    # RuleApi.query_rule()
    # RuleApi.query_event()
    # RuleApi.query_alarm_record_list()
    # RuleApi.query_all_alarm_record_list()
    # RuleApi.creat_fb_work_by_user()
    # RuleApi.close_fb_work_by_user()
    RuleApi.delete_rule()
