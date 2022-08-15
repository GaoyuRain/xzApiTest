"""
author :admin
Date : 2021/07/16
Description :
"""
import os

hasLog = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

"""告警平台配置"""
ALARM_CENTER_URL_DEV = "https://alarm-center.dev.ennew.com"
ALARM_CENTER_URL_prod = "https://alarm-center.ennew.com"
BASEURL_API_PROD = "http://alarm-plateform-api.fnwintranet.com"
BASEURL_API_TEST = "http://alarm-plateform-api.test.fnwintranet.com"

# 老告警平台的后端项目
BASEURL_CONFIG_TEST = "http://alarm-config.test.fnwintranet.com"
BASEURL_CONFIG_PROD = "https://dp.fanneng.com/alarmCenter"

# 告警规则引擎项目
BASE_RULE_ENIGINE_TEST = "https://iot-rule-engine.dev.ennew.com"
BASE_RULE_ENIGINE_PROD = "http://iot-rule-engine.dev.ennew.com"


# alarm_config 项目测试环境 dev prod
con_env = "dev"

# alarm-plateform-api 项目测试环境 dev prod
api_env = "dev"


def get_host(proj, type):
    if "alarm_config".__eq__(proj):
        if 'dev'.__eq__(type):
            return BASEURL_CONFIG_TEST
        elif "prod".__eq__(type):
            return BASEURL_CONFIG_PROD
    elif 'alarm-plateform-api'.__eq__(proj):
        if 'dev'.__eq__(type):
            return BASEURL_API_TEST
        elif "prod".__eq__(type):
            return BASEURL_API_PROD
    elif 'alarm_center'.__eq__(proj):
        if 'dev'.__eq__(type):
            return ALARM_CENTER_URL_DEV
        elif "prod".__eq__(type):
            return ALARM_CENTER_URL_prod
    elif 'iot-rule-engine'.__eq__(proj):
        if 'dev'.__eq__(type):
            return BASE_RULE_ENIGINE_TEST
        elif "prod".__eq__(type):
            return BASE_RULE_ENIGINE_PROD


BASE_ALARM_CON_URL = get_host('alarm_config', con_env)
BASE_ALARM_API_URL = get_host('alarm-plateform-api', api_env)
BASE_ALARM_ENI_URL = get_host('alarm-plateform-api', api_env)

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
