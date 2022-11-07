import random
import subprocess
import time
from multiprocessing import Pool, Process
from typing import List

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
xz_enigne_message = {"version": "1.0", "data": [
    {"devType": "METE", "devId": "1557646223253573634", "time": str(int(TimeUtils.get_current_timestamp() / 1000)),
     "metrics": {"ACTovCurrZrSignal": 1, "ACTProtOvloadSignal": 0
                 }}]}


class AlarmConfig:
    fn_alarm_topic = "data_iot_EMS"
    apm_alarm_topic = "apm_window_result"
    xz_alarm_topic = "md-action_center-data_warehouse-topic"
    alarm_result_topic = "alarm_result"
    third_topic = "data_iot_third_part"
    fn_iot_topic = "data_iot_IOTM"
    xz_enigne_test_topic = "data_iot_menu"
    xz_enigne_test_server = "10.39.68.191:9092,10.39.68.192:9092,10.39.68.193:9092"
    bd_test_server = "10.39.52.36"
    fn_iot_test_server = "10.39.10.13:9092,10.39.10.15:9092,10.39.10.16:9092"
    hld_test_server = "10.39.82.91:29092"
    # hld_test_topic = "data_iot_huludao"
    hld_test_topic = "data_iot_metric"
    nlam_test_server = "10.39.64.34:9092"
    nlam_metric_topic = "data_iot_metric"
    nlam_event_topic = "data_iot_event"
    nlam_fat_server = "10.39.64.34:9092"

    xz_test_server = "10.39.201.43:9092,10.39.201.44:9092,10.39.201.45:9092"
    prod_server = "110.39.203.16:9092,10.39.203.15:9092,10.39.203.19:9092"
    fn_prod_server = '10.38.97.18:9092,10.38.97.10:9092,10.38.97.11:9092,10.38.97.17:9092'
    fn_iot_prod_server = '10.39.30.92:9092,10.39.30.99:9092,10.39.30.100:9092'
    xz_prod_config = [xz_prod_message, xz_alarm_topic, prod_server]
    apm_prod_config = [apm_prod_message, apm_alarm_topic, prod_server]

    @staticmethod
    def get_config(type, ruleid, value=None, env='dev', total=0):
        '''
        :param type: 消息类型 fn 泛能设备测点规则  iot 泛能离线规则 xz 新智告警规则 apm 监控告警规则
        :param ruleid: 规则id
        :param value: 触发告警的值
        :param env: 环境
        :return:
        '''
        if 'fn'.__eq__(type):
            fn_message = MessageUtils.get_fn_message(ruleid, value, env)
            if 'prod'.__eq__(env):
                fn_config = [fn_message, AlarmConfig.fn_alarm_topic, AlarmConfig.fn_prod_server]
            else:
                fn_config = [fn_message, AlarmConfig.fn_alarm_topic, AlarmConfig.bd_test_server]
            return fn_config
        elif 'iot'.__eq__(type):
            fn_iot_message = MessageUtils.get_iot_message(ruleid, env, total=total)
            if 'prod'.__eq__(env):
                fn_iot_config = [fn_iot_message, AlarmConfig.fn_iot_topic, AlarmConfig.fn_iot_prod_server]
            else:
                fn_iot_config = [fn_iot_message, AlarmConfig.fn_iot_topic, AlarmConfig.fn_iot_test_server]
            return fn_iot_config
        elif 'xz'.__eq__(type):
            xz_message = MessageUtils.get_xz_message(1496774521609191424, 105, '154761f6003644e3ade8c4d252116b67')
            xz_config = [xz_message, AlarmConfig.xz_alarm_topic, AlarmConfig.xz_test_server]
            return xz_config
        elif 'apm'.__eq__(type):
            apm_message01 = MessageUtils.get_apm_message(1495996855845318656, 101.108)
            apm_config = [apm_message01, AlarmConfig.apm_alarm_topic, AlarmConfig.xz_test_server]
            return apm_config
        elif 'enigne'.__eq__(type):
            message = MessageUtils.get_enigine_message(ruleid, value, 'enigne')
            enigne_config = [message, AlarmConfig.xz_enigne_test_topic, AlarmConfig.xz_enigne_test_server]
            return enigne_config
        elif 'hld'.__eq__(type):
            message = MessageUtils.get_enigine_message(ruleid, value, 'hld')
            enigne_config = [message, AlarmConfig.hld_test_topic, AlarmConfig.hld_test_server]
            return enigne_config
        elif 'nalm_metric'.__eq__(type):
            message = MessageUtils.get_new_alarm_message(ruleid, rule_type=0, value=value)
            enigne_config = [message, AlarmConfig.nlam_metric_topic, AlarmConfig.nlam_test_server]
            return enigne_config
        elif 'nalm_event'.__eq__(type):
            message = MessageUtils.get_new_alarm_message(ruleid, rule_type=2, value=value)
            enigne_config = [message, AlarmConfig.nlam_event_topic, AlarmConfig.nlam_test_server]
            return enigne_config


def send_kfmsg(config):
    # data_list = [fn_message02, fn_message01]
    # data_list = [fn_stbk_message]
    data_list = config[0] if isinstance(config[0], List) else [config[0]]
    print(data_list)
    kp = KProducer(topic=config[1], bootstrap_servers=config[2])
    # print(data_list)
    pastition = kp.sync_producer(data_list)
    return pastition


if __name__ == '__main__':
    # send_kfmsg(AlarmConfig.get_config('fn', 1037061336687394816, 700, 'prod'))
    # send_kfmsg(AlarmConfig.get_config('enigne', 1585145749287530496, 913))
    # send_kfmsg(AlarmConfig.get_config('nalm_metric', 1588425757567471616, 345))
    # send_kfmsg(AlarmConfig.get_config('nalm_event', 1588425757567471616, 306))
    # todo 先表里设置为None
    send_kfmsg(AlarmConfig.get_config('hld', 1580386248758210560, 10.6))
    # send_kfmsg(AlarmConfig.get_config('fn', 1017742472117997568, 1.0, 'dev'))
    # send_kfmsg(AlarmConfig.get_config('fn', 1017741490587947008, 100, 'dev'))
    # send_kfmsg(AlarmConfig.get_config('fn', 1012012069373050880, 96, 'dev'))
    # send_kfmsg(AlarmConfig.get_config('enigne', 111))
    # send_kfmsg(AlarmConfig.get_config('fn', 1009898132891492352, 1.0, 'dev'))
    # 996814957694881792
    # 17:52在线  编辑规则立即告警
    # send_kfmsg(AlarmConfig.get_config('iot', 1024254574959464448, env='dev',total=0))
    # send_kfmsg(AlarmConfig.get_config('iot', 1006558976094937088, env='dev',total=0))
    # send_kfmsg(AlarmConfig.get_config('iot', 1006615710756028416, env='prod'))
    # for i in range(3):
    #     # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
    #     p = Process(target=send_kfmsg, args=(AlarmConfig.fn_config,))
    #     p.start()
    #     p.join()
    #     time.sleep(5)
