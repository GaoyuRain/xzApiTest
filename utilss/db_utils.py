"""
author :admin
Date : 2022/08/19
Description : 数据库工具，获取规则信息等
"""
from utilss.cutstom_exception import RuleStatusError
from utilss.time_utils import TimeUtils


class DBUtils:

    @staticmethod
    def check_rule_status(status, updateTime):
        if status == 0:
            raise RuleStatusError('规则未启用')
        changeTime = int(TimeUtils.get_current_timestamp() / 1000 - TimeUtils.get_current_timestamp(updateTime) / 1000)
        if changeTime < 300:
            raise RuleStatusError(f'规则最近更新时间:{updateTime},未超过5分钟')


if __name__ == '__main__':
    DBUtils.check_rule_status(1, "2022-08-19 15:05:00")
