"""
author :admin
Date : 2022/08/19
Description : 异常
"""


class RuleStatusError(Exception):
    def __init__(self, message):
        self.message = message
