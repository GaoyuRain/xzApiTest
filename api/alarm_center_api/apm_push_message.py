"""
author :admin
Date : 2021/12/28
Description :
"""

# ctime = '2021-12-06 18:46:00'
from utilss.kafka_data_utils import KProducer
from utilss.message_utils import MessageUtils
from utilss.time_utils import TimeUtils

ctime = TimeUtils.get_current_timestamp()
# test
apm_message = MessageUtils.get_apm_message(1476478101469925376)

apm_alarm_topic = "apm_window_result"
xz_test_server = "10.39.201.43:9092,10.39.201.44:9092,10.39.201.45:9092"

apm_config = [apm_message, apm_alarm_topic, xz_test_server]


def send_kfmsg(config):
    # data_list = [fn_message02, fn_message01]
    # data_list = [fn_stbk_message]
    data_list = [config[0]]
    kp = KProducer(topic=config[1], bootstrap_servers=config[2])
    kp.sync_producer(data_list)


if __name__ == '__main__':
    send_kfmsg(apm_config)
