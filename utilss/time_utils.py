"""
author :admin
Date : 2021/09/30
Description :
"""
import datetime
import time


class TimeUtils:

    @staticmethod
    def get_current_timestamp(strtime=None):
        """
        :param strtime: 格式：2021-10-08 10:13:00
        :return: 时间戳 13位
        """
        # 获取当前时间的时间戳
        if strtime is None:
            return int(round(time.time() * 1000))
        # 获取指定时间的时间戳
        timeArray = time.strptime(strtime, "%Y-%m-%d %H:%M:%S")
        timestamp = int(time.mktime(timeArray) * 1000)
        return timestamp

    @staticmethod
    def get_ctime_from_timestamp(itime):
        '''
        时间戳转换为时间
        :param itime:
        :return:
        '''
        if len(str(itime)) == 13:
            itime = itime / 1000
        timeArray = time.localtime(itime)
        print(timeArray)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        print(otherStyleTime)

    @staticmethod
    def get_ctime():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() / 1000)))
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    dt = "2021-09-30 16:24:00"
    # # 转换成时间数组
    # timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # timestamp = int(time.mktime(timeArray) * 1000)
    # print(int(timestamp * 1000))
    # print(time.ctime())
    # print(TimeUtils.get_current_timestamp())
    # TimeUtils.get_ctime_from_timestamp(1638424440625)
