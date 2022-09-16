"""
author :admin
Date : 2022/08/30
Description :
"""
import subprocess

from locust import TaskSet, HttpUser, between, task

from constant import BASE_ALARM_API_URL
from utilss.data_utils import DataUtils


class AlarmApiTest(HttpUser):
    def on_start(self):
        # dev
        self.cookie = {"fnw_token": "MTQwMzI3MzA1MTIyMTgzOTg3MyM0OUJFNzMxNC04MzcyLTQ2REUtQTJBNS0zOTQxNkY3RDExQUIPCPC"}
        # prod
        # self.cookie = {"fnw_token": "MTQ2MjA1MTQyMzMwOTA2NjI0MiMwNEZFNTI4OS0yMzRFLTQxMTEtOEZFOC1FNDlFNjM4QTA1NzEPCPC"}
        self.params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/get_alarm_infos_data.json')
        # self.params = DataUtils.get_json_data('alarm_center_api_data', '/ck_es_data/get_alarm_infos_data_prod.json')

    @task
    def get_alarm_infos(self):
        url = "/getAlarmInfos"
        self.client.post(url, cookies=self.cookie, json=self.params, name=url)


class WebsiteUser(HttpUser):
    host = BASE_ALARM_API_URL
    wait_time = between(5, 10)
    tasks = [AlarmApiTest]


if __name__ == '__main__':
    # 60s十条左右
    l_cmd_noweb = 'locust -f ../script/alarm_api_locust.py  --headless -u 50 -r 2 --run-time 600s  --stop-timeout 20'
    l_cmd = 'locust -f ../script/alarm_api_locust.py'
    subprocess.call(l_cmd, shell=True)
