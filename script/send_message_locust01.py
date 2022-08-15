"""
author :admin
Date : 2022/07/01
Description : 批量发送设备消息
"""
import random
import subprocess
import time
from typing import List

from locust import TaskSet, task, HttpUser, between

from utilss.kafka_data_utils import KProducer
from utilss.message_utils import MessageUtils
from utilss.time_utils import TimeUtils

fn_prod_server = '10.38.97.18:9092,10.38.97.10:9092,10.38.97.11:9092,10.38.97.17:9092'

class AlarmMessageTest(TaskSet):
    def on_start(self):
        self.num = 0
        self.fn_iot_message: List = MessageUtils.get_iot_message(1006558976094937088, env='dev', total=0)

    # @task
    # def send_kfmsg(self):
    #     data_list = [MessageUtils.get_fn_message(997521637005004800, random.randint(300, 500))]
    #     kp = KProducer(topic="data_iot_EMS", bootstrap_servers="10.39.52.36")
    #     pastition = kp.sync_producer(data_list)
    #     time.sleep(2)
    #     self.num = self.num + 1

    @task
    def send_kfmsg_iot(self):
        # test
        kp = KProducer(topic="data_iot_IOTM", bootstrap_servers="10.39.10.13:9092,10.39.10.15:9092,10.39.10.16:9092")
        # prod
        # kp = KProducer(topic="data_iot_IOTM", bootstrap_servers="10.38.97.18:9092,10.38.97.10:9092,10.38.97.11:9092,10.38.97.17:9092")
        ctime = TimeUtils.get_current_timestamp()
        for i in range(self.fn_iot_message.__len__()):
            self.fn_iot_message[i][0].update({'time': ctime})
            self.fn_iot_message[i][0].get('metrics').update({'connected.time': ctime})
        pastition = kp.sync_producer(self.fn_iot_message)
        time.sleep(1)
        self.num = self.num + 1

    def on_stop(self):
        print('总执行次数：', self.num)


class WebsiteUser(HttpUser):
    host = ''
    wait_time = between(30, 40)
    tasks = [AlarmMessageTest]


if __name__ == '__main__':
    # 60s十条左右
    l_cmd = 'locust -f ../script/send_message_locust01.py  --headless -u 1 -r 1 --run-time 2h  --stop-timeout 20'
    subprocess.call(l_cmd, shell=True)
