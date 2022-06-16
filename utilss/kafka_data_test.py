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
fn_alarm_topic = "data_iot_EMS"
apm_alarm_topic = "apm_window_result"
xz_alarm_topic = "md-action_center-data_warehouse-topic"
alarm_result_topic = "alarm_result"
third_topic = "data_iot_third_part"
bd_test_server = "10.39.52.36"

xz_test_server = "10.39.201.43:9092,10.39.201.44:9092,10.39.201.45:9092"
prod_server = "110.39.203.16:9092,10.39.203.15:9092,10.39.203.19:9092"


class AlarmConfig:
    ctime = TimeUtils.get_current_timestamp()

    # 1529398360946343936
    # fn_message = MessageUtils.get_fn_message(1531180155047780352, 901)
    fn_message = MessageUtils.get_fn_message(975829829015928832, 111)
    apm_message01 = MessageUtils.get_apm_message(1495996855845318656, 101.108)
    xz_message = MessageUtils.get_xz_message(1496774521609191424, 105, '154761f6003644e3ade8c4d252116b67')
    fn_config = [fn_message, fn_alarm_topic, bd_test_server]
    apm_config = [apm_message01, apm_alarm_topic, xz_test_server]
    xz_config = [xz_message, xz_alarm_topic, xz_test_server]
    # fn_third_config = [fn_message, third_topic, bd_test_server]

    xz_prod_config = [xz_prod_message, xz_alarm_topic, prod_server]
    apm_prod_config = [apm_prod_message, apm_alarm_topic, prod_server]

    alarm_message = MessageUtils.get_alarm_message(18438, "f1fcd8e14314414f99d48bfacd845528", 300)


def send_kfmsg(config):
    # data_list = [fn_message02, fn_message01]
    # data_list = [fn_stbk_message]
    data_list = [config[0]]
    kp = KProducer(topic=config[1], bootstrap_servers=config[2])
    kp.sync_producer(data_list)


if __name__ == '__main__':
    # send_kfmsg(AlarmConfig.apm_prod_config)
    # send_kfmsg(AlarmConfig.apm_config)
    # send_kfmsg(AlarmConfig.fn_third_config)
    # time.sleep(2)
    send_kfmsg(AlarmConfig.fn_config)
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



