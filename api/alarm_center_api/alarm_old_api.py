"""
author :admin
Date : 2022/02/25
Description :
"""


class AlarmApi:
    @classmethod
    def getAlarmHistoryPageByInstanceIdAndDate(cls):
        params = {{"alarmStatus": 0,"eTriggerTime": "",
            "entId": "",
            "equipIds": [],
            "equipName": "",
            "eventId": 0,
            "instanceId": 0,
            "pageIndex": 0,
            "pageSize": 0,
            "resultId": 0,
            "ruleEntId": "",
            "sTriggerTime": "",
            "staId": "",
            "translate": True
        }}
