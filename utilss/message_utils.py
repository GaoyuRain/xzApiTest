import base64
import copy
import json

import pymysql

# test
from utilss.db_utils import DBUtils
from utilss.time_utils import TimeUtils


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
    def get_fn_message(cls, ruleid, value, env='dev'):
        fn_message01 = {"staId": "PARK172_EMS01", "data": [], "domain": "EMS", "allPoints": 1, "version": "0.0.1"}
        data_info = []
        if "prod".__eq__(env) is True:
            try:
                # 老平台数据库 prod
                conn = pymysql.connect(host='10.39.45.74', port=3306, user='alarm_plateform_slave',
                                       password='4kFG3lMxR7Nu',
                                       db='alarm_plateform', charset='utf8', use_unicode=True)
                cur = conn.cursor()
                sql = f'SELECT sta_id,domain,equip_id,alarm_desc_map,rule_id,rule_status,update_time FROM alarm_instance_info WHERE id={ruleid}  order by id Desc LIMIT 1;'
                cur.execute(sql)
                data_info = list(cur.fetchone())
            except Exception as result:
                print("错误: %s" % result)
            finally:
                cur.close()
                conn.close()
        else:
            # 老平台数据库 test
            conn = pymysql.connect(host='10.39.30.21', user='fn_db_test', password='fn_db_test20180411',
                                   db='alarm-plateform', charset='utf8'
                                   # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
                                   )
            cur = conn.cursor()
            sql = f'SELECT sta_id,domain,equip_id,alarm_desc_map,rule_id,rule_status,update_time FROM alarm_instance_info WHERE id={ruleid}  order by id Desc LIMIT 1;'
            cur.execute(sql)
            data_info = list(cur.fetchone())
            cur.close()
            conn.close()
            # print('data_info：',data_info)
        new_ruleid = data_info[4]
        print(f'new_ruid: {new_ruleid}')
        metric = data_info[2] + '_' + str(json.loads(data_info[3])[0].get("code"))
        fn_message01.update({"staId": data_info[0], "domain": data_info[1],
                             "data": [
                                 {"metric": metric, "time": TimeUtils.get_current_timestamp(), "value": str(value)}]})
        print(fn_message01)
        DBUtils.check_rule_status(int(data_info[5]), str(data_info[6]))
        return fn_message01

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
    def get_iot_message(cls, ruleid, env='dev', total=0):
        '''
        :param ruleid: 规则id
        :param env:  环境
        :param total: 共获取几个设备的消息 0:全部
        :return:
        '''
        data_info = []
        sta_id = 'sta_id'
        entity_id = 'FN05GD1214'
        message = [{"domain": "IOTM", "v": "1", "time": TimeUtils.get_current_timestamp(),
                    "tags": {
                        "systemCode": 'sta_id',
                        "appId": "iot-gateway-dtu",
                        "gatewayId": 'entity_id'
                    }, "metrics": {
                "gateway.s.online": 1,
                "connected.time": TimeUtils.get_current_timestamp(),
                "online.status": 1
            }}]
        if "prod".__eq__(env) is True:
            try:
                # 老平台数据库 prod
                conn = pymysql.connect(host='10.39.45.74', port=3306, user='alarm_plateform_slave',
                                       password='4kFG3lMxR7Nu',
                                       db='alarm_plateform', charset='utf8', use_unicode=True)
                cur = conn.cursor()
                sql = f'SELECT rule_id,sta_id FROM alarm_instance_info WHERE id={ruleid}  order by id Desc ;'
                cur.execute(sql)
                data_info = list(cur.fetchone())
                new_ruleid = data_info[0]
                sta_id = data_info[1]
                print(data_info)

                # 新平台数据库
                conn1 = pymysql.connect(host='192.168.235.237', user='alarm_center_rw', password='dJcNNw5jOir%',
                                        db='alarm_center', charset='utf8'
                                        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
                                        )
                cur1 = conn1.cursor()
                sql1 = f'SELECT entity_id FROM rule_object WHERE rule_id={new_ruleid}  order by id Desc ;'
                cur1.execute(sql1)
                info1 = list(cur1.fetchall())
                print(f'info1:{info1}')

            except Exception as result:
                print("错误: %s" % result)
            finally:
                cur.close()
                conn.close()
                cur1.close()
                conn1.close()
        else:
            # 老平台数据库 dev
            conn = pymysql.connect(host='10.39.30.21', user='fn_db_test', password='fn_db_test20180411',
                                   db='alarm-plateform', charset='utf8'
                                   # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
                                   )
            cur = conn.cursor()

            sql = f'SELECT rule_id,sta_id FROM alarm_instance_info WHERE id={ruleid}  order by id Desc;'
            cur.execute(sql)
            data_info = list(cur.fetchone())
            new_ruleid = data_info[0]
            sta_id = data_info[1]
            cur.close()
            conn.close()
            print(f'new_ruid: {new_ruleid}')
            # 新平台数据库
            conn1 = pymysql.connect(host='10.39.202.254', user='alarm_center_rw', password='Fm9l^hnnjlP*',
                                    db='alarm_center', charset='utf8'
                                    # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
                                    )
            cur1 = conn1.cursor()
            sql1 = f'SELECT entity_id FROM rule_object WHERE rule_id={new_ruleid}  order by id Desc;'
            cur1.execute(sql1)
            info1 = list(cur1.fetchall())
            print(f'info1:{info1}')
            cur1.close()
            conn1.close()
        if total > total > info1.__len__() or total == 0:
            total = info1.__len__()
        print(f'total={total}')
        message_list = []
        for i in range(total):
            entity_id = info1[i][0]
            data_message = copy.deepcopy(message)
            data_message[0].get('tags').update({"systemCode": sta_id + '_test_gy', "gatewayId": entity_id})
            message_list.append(data_message)
        print(message_list)
        return message_list

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
    # MessageUtils.get_fn_message(998525905103761408, 20, 'dev')
    MessageUtils.get_fn_message(998525905103761408, 60)
    # 设备掉线 WB01GD2211
    # MessageUtils.get_iot_message(1003717540105113600,env='prod', total=0)
    # MessageUtils.get_iot_message(1006247075699924992, env='dev', total=0)
    # print('-----------------------------------------------------------------------')
    # MessageUtils.get_iot_message(999348874524766208, 'test')
    # MessageUtils.get_xz_message(1485857764544606208, 100, 'ffd27f05dcc14ba7841e914c5ef2c6f1')
