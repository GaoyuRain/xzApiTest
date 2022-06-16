import base64
import json

import pymysql

# test
from time_utils import TimeUtils


class MessageUtils:
    apm_message01 = {
        "date": TimeUtils.get_current_timestamp(),
        "ext": "",
        "metricKey": {"metricId": "", "metric": "", "locationId": "", "domain": "", "entityId": "", "tag": ""},
        "isVirtualMetric": False,
        "updateTime": TimeUtils.get_current_timestamp(),
        "value": "8.0"}
    fn_message01 = {
        "staId": "PARK172_EMS01",
        "data": [],
        "domain": "EMS",
        "allPoints": 1,
        "version": "0.0.1"}

    xz_message = {
        "header": {
            "version": "1.0"
        }, "body": [
            {
                "metric": "Qc",
                "valueNum": 0,
                "tags": {
                    "deviceNumber": "PARK1037_EMS01-METE_METE436",
                    "status": 1,
                    "anomalousCode": 0
                },
                "ts": 1642411140000
            }]}

    @classmethod
    def get_apm_message(cls, ruleid, value):
        conn = pymysql.connect(host='10.39.202.254', user='alarm_center_rw', password='Fm9l^hnnjlP*',
                               db='alarm_center', charset='utf8'
                               # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
                               )
        cur = conn.cursor()
        sql = f'SELECT location_id,tag,entity_id,metric FROM rule_engine_variable WHERE rule_id={ruleid}  order by id Desc LIMIT 1;'
        result = cur.execute(sql)
        info = list(cur.fetchone())
        # print(info)
        metricId = str(base64.b64encode(info[2].encode()), "utf-8") + ".1." + info[0]
        print("metricId:" + metricId)
        cur.close()
        conn.close()
        metricKey = {'metricKey': {"metricId": metricId, "metric": info[3], "locationId": info[0],
                                   "domain": "APM", "entityId": info[2], "tag": info[1]}}
        cls.apm_message01.update(metricKey)
        cls.apm_message01.update({"value": str(value)})
        print(cls.apm_message01)
        return cls.apm_message01

    @classmethod
    def get_fn_message1(cls, ruleid, value):

        # 新平台数据库
        conn2 = pymysql.connect(host='10.39.202.254', user='alarm_center_rw', password='Fm9l^hnnjlP*',
                                db='alarm_center', charset='utf8'
                                # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
                                )
        cur2 = conn2.cursor()
        sql = f'SELECT location_id,domain,entity_id,metric FROM rule_engine_variable WHERE rule_id={ruleid}  order by id Desc LIMIT 1;'
        result = cur2.execute(sql)
        info = list(cur2.fetchone())
        metric = info[3] if info[2] is None else info[2] + '_' + info[3]
        cls.fn_message01.update({"staId": info[0], "domain": info[1],
                                 "data": [
                                     {"metric": metric, "time": TimeUtils.get_current_timestamp(), "value": str(value)}
                                     # ,{"metric": "METE_METE01_Ua", "time": TimeUtils.get_current_timestamp(),"value": str(value)
                                 ]})
        print(cls.fn_message01)
        cur2.close()
        conn2.close()
        return cls.fn_message01

    @classmethod
    def get_fn_message(cls, ruleid, value):
        # 老平台数据库
        conn = pymysql.connect(host='10.39.30.21', user='fn_db_test', password='fn_db_test20180411',
                               db='alarm-plateform', charset='utf8'
                               # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
                               )
        cur = conn.cursor()
        sql = f'SELECT sta_id,domain,equip_id,alarm_desc_map,rule_id FROM alarm_instance_info WHERE id={ruleid}  order by id Desc LIMIT 1;'

        cur.execute(sql)
        info = list(cur.fetchone())
        new_ruleid = info[4]
        print(f'new_ruid: {new_ruleid}')

        metric = info[2] + '_' + str(json.loads(info[3])[0].get("code"))
        cls.fn_message01.update({"staId": info[0], "domain": info[1],
                                 "data": [
                                     {"metric": metric, "time": TimeUtils.get_current_timestamp(), "value": str(value)}
                                     # ,{"metric": "METE_METE01_Ua", "time": TimeUtils.get_current_timestamp(),"value": str(value)
                                 ]})
        print(cls.fn_message01)
        cur.close()
        conn.close()
        return cls.fn_message01

    @classmethod
    def get_xz_message(cls, ruleid, value, devicenumber):
        conn = pymysql.connect(host='10.39.202.254', user='alarm_center_rw', password='Fm9l^hnnjlP*',
                               db='alarm_center', charset='utf8'
                               # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
                               )
        cur = conn.cursor()
        xz_message01 = {
            "date": TimeUtils.get_current_timestamp(),
            "metricKey": {"metric": "", "locationId": "ENNEW", "domain": "ENNEW", "tag": "ENNEW"},
            "allPoints": 1,
            "updateTime": TimeUtils.get_current_timestamp(),
            "version": "0.0.1"}
        sql = f'SELECT location_id,tag,entity_id,metric FROM rule_engine_variable WHERE rule_id={ruleid} order by id Desc LIMIT 1;'

        result = cur.execute(sql)
        info = list(cur.fetchone())
        # print(info)
        cur.close()
        conn.close()
        xz_message = {"header": {"version": "1.0"},
                      "body": [{"metric": info[3], "valueNum": value,
                                "tags": {"deviceNumber": devicenumber,
                                         "status": 1,
                                         "anomalousCode": 0},
                                "ts": TimeUtils.get_current_timestamp()
                                }]}
        metricKey = {
            'metricKey': {"deviceNumber": devicenumber, "metric": info[3], "locationId": info[0], "domain": "ENNEW",
                          "tag": "ENNEW"}}
        xz_message01.update(metricKey)
        xz_message01.update({"value": str(value)})
        print(xz_message)
        return xz_message

    @classmethod
    def get_alarm_message(cls, expid, code, value):
        alarm_message = {
            "expressionId": expid,
            "locationId": "ENNEW",
            "domain": "ENNEW",
            "tenantId": "ENNEW",
            "entityId": code,
            "triggerTime": str(TimeUtils.get_ctime()),
            "MetricData": {
                "C0": [{
                    "date": str(TimeUtils.get_ctime()),
                    "value": str(value)
                },
                    {
                        "date": str(TimeUtils.get_ctime()),
                        "value": str(value)
                    }]
            }
        }
        alarm_message = {'expressionId': 18438, 'locationId': 'ENNEW', 'domain': 'ENNEW', 'tenantId': 'ENNEW',
                         'entityId': '20e76e80cf6c48f6aa7d747558e638af', 'triggerTime': '2022-01-18 15:13:07',
                         'MetricData': {'C0': [{'date': '2022-01-18 15:14:07', 'value': '300'},
                                               {'date': '2022-01-18 15:13:07', 'value': '300'}]}}

        print(alarm_message)
        return alarm_message

    @classmethod
    def get_message(cls, type, ruleid, value, deviceNumber=None):
        '''
        :param type:  apm 或者 fanNeng
        :param ruleid: 规则id
        :param value:  测点值
        :return: 测点消息
        '''
        if "apm".__eq__(type):
            return cls.get_apm_message(ruleid, value)
        elif "xz".__eq__(type):
            return cls.get_xz_message(ruleid, value, deviceNumber)
        else:
            return cls.get_fn_message(ruleid, value)


if __name__ == '__main__':
    # MessageUtils.get_apm_message(1475731876462333952)
    MessageUtils.get_fn_message1(984106669903163392, 20)
    # MessageUtils.get_fn_message(984106669903163392, 20)
    # MessageUtils.get_xz_message(1485857764544606208, 100, 'ffd27f05dcc14ba7841e914c5ef2c6f1')
