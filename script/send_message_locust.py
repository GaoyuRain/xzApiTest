"""
author :admin
Date : 2022/07/01
Description : 批量发送设备消息
"""
import random
import subprocess
import time

from locust import TaskSet, task, HttpUser, between

from utilss.kafka_data_utils import KProducer
from utilss.message_utils import MessageUtils


class AlarmMessageTest(TaskSet):
    def on_start(self):
        self.num = 0

    @task
    def send_kfmsg(self):
        data_list = [MessageUtils.get_fn_message(990985826044919808, random.randint(200, 500))]
        kp = KProducer(topic="data_iot_EMS", bootstrap_servers="10.39.52.36")
        pastition = kp.sync_producer(data_list)
        time.sleep(2)
        self.num = self.num + 1

    def on_stop(self):
        print('总执行次数：', self.num)


class WebsiteUser(HttpUser):
    host = ''
    wait_time = between(1, 3)
    tasks = [AlarmMessageTest]


if __name__ == '__main__':
    # 60s十条左右
    l_cmd = 'locust -f ../script/send_message_locust.py  --headless -u 1 -r 1 --run-time 60s  --stop-timeout 20'
    subprocess.call(l_cmd, shell=True)
