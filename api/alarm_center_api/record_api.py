"""
author :admin
Date : 2021/09/17
Description :
"""
import requests

from constant import ALARM_BASER_URL_DEV

alarmBody = '''{"expressionId":62,"triggerTime":"2021-09-07 23:01:13","MetricData":{"C0":[{"date":"2021-09-07 23:01:00"
,"value":"10375.531"},{"date":"2021-09-07 23:00:00","value":"10397.643"}]}}'''


class RecordApi:

    @staticmethod
    def add_alarm_record():
        url = ALARM_BASER_URL_DEV + '/alarmRecord/add'
        params = {"alarmBody": alarmBody, "alarmLevel": 1, "alarmTime": "2021-09-17 12:41:09", "alarmType": 0,
                  'id': 10086,
                  "ruleId": 1437345007030898688}
        r = requests.post(url, json=params, timeout=10)
        print(r.status_code)
        print(r.json())


if __name__ == '__main__':
    RecordApi.add_alarm_record()
