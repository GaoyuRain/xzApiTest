"""
author :admin
Date : 2021/09/30
Description :
"""
import copy
import json
import time

from kafka import KafkaProducer

from utilss.time_utils import TimeUtils


class KProducer:
    def __init__(self, bootstrap_servers, topic):
        """
        kafka 生产者
        :param bootstrap_servers: 地址
        :param topic:  topic
         security_protocol="SSL"
        """
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda m: json.dumps(m).encode('ascii'))  # json 格式化发送的内容
        self.topic = topic

    def sync_producer(self, data_li: list):
        """
        同步发送 数据
        :param data_li:  发送数据
        :return:
        """
        for data in data_li:
            future = self.producer.send(self.topic, data)
            record_metadata = future.get(timeout=30)  # 同步确认消费
            partition = record_metadata.partition  # 数据所在的分区
            offset = record_metadata.offset  # 数据所在分区的位置
            print('save success, partition: {}, offset: {}'.format(partition, offset))

    def asyn1_producer(self, data_li: list):
        """
        异步发送数据
        :param data_li:发送数据
        :return:
        """
        for data in data_li:
            self.producer.send(self.topic, data)
        self.producer.flush()  # 批量提交

    def asyn1_producer_callback(self, data_li: list):
        """
        异步发送数据 + 发送状态处理
        :param data_li:发送数据
        :return:
        """
        for data in data_li:
            self.producer.send(self.topic, data).add_callback(self.send_success).add_errback(self.send_error)
        self.producer.flush()  # 批量提交

    def send_success(self, *args, **kwargs):
        """异步发送成功回调函数"""
        print('save success')
        return

    def send_error(self, *args, **kwargs):
        """异步发送错误回调函数"""
        print('save error')
        return

    def close_producer(self):
        try:
            self.producer.close()
        except:
            pass


if __name__ == '__main__':
    gd_message = {"memo": "工单(904338542939648405)已关闭, 请查看", "msgType": "closeWorkOrder", "state": 9,
                  "tenantId": "1369559970221985794", "workId": "904338542939648405"}

    message = {
        "staId": "PARK1037_EMS01",
        "data": [{"metric": "METE_METE11_Ua",
                  # "2021-10-13 15:39:00"
                  "time": TimeUtils.get_current_timestamp(), "value": "300.0"}],
        "domain": "EMS",
        "allPoints": 1,
        "version": "0.0.1"}

    data_list = [gd_message]
    # kp = KProducer(topic='data_iot_EMS', bootstrap_servers="10.39.52.36")
    kp = KProducer(topic='enn-sale-oms-workorder-terminal-topic', bootstrap_servers="10.39.52.36")
    kp.sync_producer(data_list)
