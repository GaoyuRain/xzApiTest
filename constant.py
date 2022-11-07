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
BASEURL_CONFIG_PROD = "https://alarm-config.fanneng.com"
# BASEURL_CONFIG_PROD = "https://dp.fanneng.com/alarmCenter"

# 告警规则引擎项目
BASE_RULE_ENIGINE_TEST = "https://iot-rule-engine.dev.ennew.com"
BASE_RULE_ENIGINE_PROD = "http://iot-rule-engine.dev.ennew.com"

# alarm_config 项目测试环境 dev prod
con_env = "prod"

# alarm-plateform-api 项目测试环境 dev prod
api_env = "prod"


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

# 数据库配置
# 老平台数据库 test
# conn = pymysql.connect(host='10.39.30.21', user='fn_db_test', password='fn_db_test20180411',
#                        db='alarm-plateform', charset='utf8'
#                        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
#                        )
# cur = conn.cursor()
# sql = f'SELECT sta_id,domain,equip_id,alarm_desc_map,rule_id,rule_status,update_time FROM alarm_instance_info WHERE id={ruleid}  order by id Desc LIMIT 1;'

ALM_CON_DEV_DBHOST = "10.39.30.21"
ALM_CON_DEV_DB = "alarm-plateform"
ALM_CON_DEV_UNAME = "fn_db_test"
ALM_CON_DEV_PWD = "fn_db_test20180411"
ALM_CON_DEV_DBCON = [ALM_CON_DEV_DBHOST, ALM_CON_DEV_UNAME, ALM_CON_DEV_PWD, ALM_CON_DEV_DB]

ENIGINE_DEV_DBHOST = "10.39.202.254"
ENIGINE_DEV_DB = "iot_rule_engine"
ENIGINE_IOTWEB_DEV_DB = "iot-alarm-web"
ENIGINE_DEV_UNAME = "alarm_center_rw"
ENIGINE_DEV_PWD = "Fm9l^hnnjlP*"
ENIGINE_DEV_DBCON = [ENIGINE_DEV_DBHOST, ENIGINE_DEV_UNAME, ENIGINE_DEV_PWD, ENIGINE_DEV_DB]
ENIGINE_IOTWEB_DEV_DBCON = [ENIGINE_DEV_DBHOST, ENIGINE_DEV_UNAME, ENIGINE_DEV_PWD, ENIGINE_IOTWEB_DEV_DB]

HLD_DEV_DBHOST = "10.39.82.91"
HLD_ENIGINE_DEV_DB = "iot_rule_engine"
HLD_ENIGINE_IOTWEB_DEV_DB = "iot_alarm_web"
HLD_DEV_UNAME = "root"
HLD_DEV_PWD = "root@123"
HLD_ENIGINE_DEV_DBCON = [HLD_DEV_DBHOST, HLD_DEV_UNAME, HLD_DEV_PWD, HLD_ENIGINE_DEV_DB]
HLD_ENIGINE_IOTWEB_DEV_DBCON = [HLD_DEV_DBHOST, HLD_DEV_UNAME, HLD_DEV_PWD, HLD_ENIGINE_IOTWEB_DEV_DB]

# 新告警中心配置
NEW_ALM_DEV_DBHOST = "10.39.64.34"
NEW_ALM_DEV_DB = "entity_model"
NEW_ALM__DEV_UNAME = "root"
NEW_ALM__DEV_PWD = "root"
NEW_ALM_DEV_DBCON = [NEW_ALM_DEV_DBHOST, NEW_ALM__DEV_UNAME, NEW_ALM__DEV_PWD, NEW_ALM_DEV_DB]

NEW_ALM_FAT_DBHOST = "10.39.68.62"
NEW_ALM_FAT_DB = "entity_model"
NEW_ALM_FAT_UNAME = "adm_airecon"
NEW_ALM_FAT_PWD = "adm2o3rhU$2i"
NEW_ALM_FAT_DBCON = [NEW_ALM_FAT_DBHOST, NEW_ALM_FAT_UNAME, NEW_ALM_FAT_PWD, NEW_ALM_FAT_DB]

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
