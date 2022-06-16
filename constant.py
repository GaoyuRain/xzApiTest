"""
author :admin
Date : 2021/07/16
Description :
"""
import os

hasLog = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

"""告警平台配置"""
ALARM_BASER_URL_DEV = "https://alarm-center.dev.ennew.com"
ALARM_BASER_URL_prod = "https://alarm-center.ennew.com"

"""AI配置"""
# 将获取到的token，以"X-GW-Authorization"为key值放到头信息中。
# dev环境账号：
# appId： O61fVMWi
# app_key: 326aecb3-5724-471b-bae5-afbc2707004f
# app_secret: UG55TkJzZENwbmFxVDBSN3hkTXlMTUJtUTQ1RmtuNUJpcVNFbGRIQXdwNlhLRURSY3VkVktXRlBWMDdQNnZUZA==
# dev环境地址： http://open-platform-gateway.dev.ennewi.cn/应用标识/接口地址

TEST_BASE_URL = 'http://middle-open-platform.dev.ennewi.cn'

AI_BASE_URL = 'http://open-platform-gateway.dev.ennewi.cn'
AI_PLATFORM_BASE_URL = 'https://ai-platform-support.dev.ennew.com'

app_id = 'O61fVMWi'
app_key = '326aecb3-5724-471b-bae5-afbc2707004f'
app_secret = 'UG55TkJzZENwbmFxVDBSN3hkTXlMTUJtUTQ1RmtuNUJpcVNFbGRIQXdwNlhLRURSY3VkVktXRlBWMDdQNnZUZA=='

HEADER = {
    'X-GW-Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjBkeWF3UThlIiwiZXhwIjoxNjM2NTE0NDIwfQ.G-lQMiGlQFcrQ4aGnH_BjI1siW2zmKQ4-cqWSLc8Jzs'}
