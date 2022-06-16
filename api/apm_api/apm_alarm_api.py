"""
author :admin
Date : 2021/11/17
Description : 监控平台告警相关api
"""
import requests

from utilss.data_utils import DataUtils
from utilss.log_utils import LogUtils
from utilss.time_utils import TimeUtils


class ApmAlarmApi:
    BASE_URL = 'https://apm-web.dev.ennew.com'
    HEADER = {
        'ennunifiedcsrftoken': '0ad546d571072f86d68cf9835bbbe1d5',
        'ennunifiedauthorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJVbmlmeUF1dGhTU08iLCJhdWQiOiJhdWQiLCJoYXNUZW5hbnQiOmZhbHNlLCJuYmYiOjE2MzcxOTk3NzQsImFwcElkIjoiYXBtLXdlYiIsImlzcyI6IjE0MDMyNzMwNTEyMjE4Mzk4NzMiLCJuaWNrbmFtZSI6IumrmOmbqCIsImdyYW50Y29kZSI6Ik1UUXdNekkzTXpBMU1USXlNVGd6T1RnM015TmlNMlE0Wm1VMU5ERmxNMkV4WVRCaU1XRmhNalZsWmpVeE0yTmxabVUyTkEiLCJleHAiOjE2MzcyODYxNzQsImlhdCI6MTYzNzE5OTc3NCwianRpIjoiMmU2NzBiOTYtNDQ5ZC00NWU0LWI1OGYtMzljNzE0YzliMzM1IiwidXNlcm5hbWUiOiJ0LUdBT1lVSSJ9.4gn-1WQAsFYfbmey6V8DFbwIgj3nNG8CUjJzTa9ptPaHg72Dl--LMyETUW9CaZ3eELag9IqLENJceWi29OkZR8l5N1umoYzmq7M7ywwZDSUhSIb7SBHDRLFI8DbsS6fQbuzAGTPQySWJNg3_pd6S9oOM2SCKNGYlUsuiUPPCs30'
    }

    @classmethod
    def alarm_list(cls):
        # '2021-11-17 16:35:00' 告警jvm活动守护线程数
        url = cls.BASE_URL + '/rest/query/alarm'
        startTime = '2021-11-17 16:35:00'
        params = {'startMillis': TimeUtils.get_current_timestamp(startTime),
                  'endMillis': TimeUtils.get_current_timestamp(),
                  'pageNum': 1,
                  'pageSize': 30}
        r = requests.post(url, json=params, headers=cls.HEADER, timeout=10)
        # print(r.status_code)
        # print(r.json())
        LogUtils.print_response(r, isformart=True)


if __name__ == '__main__':
    # TimeUtils.get_ctime_from_timestamp(1637136360000)
    ApmAlarmApi.alarm_list()
