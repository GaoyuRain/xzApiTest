import random
import subprocess
import time
from multiprocessing import Pool, Process

from utilss.kafka_data_utils import KProducer
from utilss.message_utils import MessageUtils
from utilss.time_utils import TimeUtils

# test
apm_prod_message = {
    "date": TimeUtils.get_current_timestamp(),
    "ext": "",
    "metricKey": {
        "metricId": "YWxhcm0tY2VudGVy.1.1369923265280311297",
        "metric": "service_cpm",
        "locationId": "1369923265280311297",
        "domain": "APM",
        "entityId": "alarm-center",
        "tag": "service"
    },
    "isVirtualMetric": False,
    "updateTime": TimeUtils.get_current_timestamp(),
    "value": "60100.0"
}
xz_prod_message = {'header': {'version': '1.0'},
                   'body': [{'metric': 'TpriSideOut', 'valueNum': 100,
                             'tags': {'deviceNumber': 'cf54a0edd7904903a24cba2b04c30827',
                                      'status': 1, 'anomalousCode': 0}, 'ts': TimeUtils.get_current_timestamp()}]}


class AlarmConfig:
    fn_alarm_topic = "data_iot_EMS"
    apm_alarm_topic = "apm_window_result"
    xz_alarm_topic = "md-action_center-data_warehouse-topic"
    alarm_result_topic = "alarm_result"
    third_topic = "data_iot_third_part"
    fn_iot_topic = "data_iot_IOTM"
    bd_test_server = "10.39.52.36"
    fn_iot_test_server = "10.39.10.13:9092,10.39.10.15:9092,10.39.10.16:9092"

    xz_test_server = "10.39.201.43:9092,10.39.201.44:9092,10.39.201.45:9092"
    prod_server = "110.39.203.16:9092,10.39.203.15:9092,10.39.203.19:9092"

    xz_prod_config = [xz_prod_message, xz_alarm_topic, prod_server]
    apm_prod_config = [apm_prod_message, apm_alarm_topic, prod_server]

    @staticmethod
    def get_config(cls, type, ruleid, value, env=None):
        if 'fn'.__eq__(type):
            fn_message = MessageUtils.get_fn_message(ruleid, value)
            fn_config = [fn_message, cls.fn_alarm_topic, cls.bd_test_server]
            return fn_config
        elif 'iot'.__eq__(type):
            fn_iot_message = MessageUtils.get_iot_message(ruleid)
            fn_iot_config = [fn_iot_message, cls.fn_iot_topic, cls.fn_iot_test_server]
            return fn_iot_config
        elif 'xz'.__eq__(type):
            xz_message = MessageUtils.get_xz_message(1496774521609191424, 105, '154761f6003644e3ade8c4d252116b67')
            xz_config = [xz_message, cls.xz_alarm_topic, cls.xz_test_server]
            return xz_config
        elif 'apm'.__eq__(type):
            apm_message01 = MessageUtils.get_apm_message(1495996855845318656, 101.108)
            apm_config = [apm_message01, cls.apm_alarm_topic, cls.xz_test_server]
            return apm_config


def send_kfmsg(config):
    # data_list = [fn_message02, fn_message01]
    # data_list = [fn_stbk_message]
    data_list = [config[0]]
    kp = KProducer(topic=config[1], bootstrap_servers=config[2])
    pastition = kp.sync_producer(data_list)
    return pastition


if __name__ == '__main__':
    # send_kfmsg(AlarmConfig.apm_prod_config)
    # send_kfmsg(AlarmConfig.apm_config)
    # send_kfmsg(AlarmConfig.fn_third_config)
    # time.sleep(2)
    # send_kfmsg(AlarmConfig.fn_config)
    send_kfmsg(AlarmConfig.get_config())
    # send_kfmsg(AlarmConfig.fn_config03)
    # time.sleep(2)

    # send_kfmsg(AlarmConfig.xz_config)
    # send_alarm_msg()

    # for i in range(3):
    #     # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
    #     p = Process(target=send_kfmsg, args=(AlarmConfig.fn_config,))
    #     p.start()
    #     p.join()
    #     time.sleep(5)

    # for i in range(5):
    #     par = send_kfmsg(AlarmConfig.fn_config)
    #     time.sleep(4)
    #     if par >= 0:
    #         continue
    #     else:
    #         time.sleep(3)
