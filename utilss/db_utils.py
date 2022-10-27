"""
author :admin
Date : 2022/08/19
Description : 数据库工具，获取规则信息等
"""
import pymysql

from constant import ALM_CON_DEV_DBCON
from utilss.cutstom_exception import RuleStatusError
from utilss.time_utils import TimeUtils


class DBUtils:
    @staticmethod
    def get_db_info(db_con: list, sql) -> list:
        conn = pymysql.connect(host=db_con[0], user=db_con[1], password=db_con[2], db=db_con[3], charset='utf8'
                               # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
                               )
        cur = conn.cursor()
        cur.execute(sql)
        data_info = list(cur.fetchall())
        cur.close()
        conn.close()
        return data_info

    @staticmethod
    def check_rule_status(status, updateTime):
        if status == 0:
            raise RuleStatusError('规则未启用')
        changeTime = int(TimeUtils.get_current_timestamp() / 1000 - TimeUtils.get_current_timestamp(updateTime) / 1000)
        if changeTime < 300:
            raise RuleStatusError(f'规则最近更新时间:{updateTime},未超过5分钟')


if __name__ == '__main__':
    DBUtils.check_rule_status(1, "2022-08-19 15:05:00")
    ruleid = 1012012060443377664
    sql = f'SELECT sta_id,domain,equip_id,alarm_desc_map,rule_id,rule_status,update_time FROM alarm_instance_info WHERE id={ruleid}  order by id Desc LIMIT 1;'
    print(DBUtils.get_db_info(ALM_CON_DEV_DBCON, sql))
