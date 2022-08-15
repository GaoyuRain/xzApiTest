"""author :rainDate : 2020/07/17Description :测试数据"""import jsonimport osimport yamlfrom constant import BASE_DIRfrom utilss.log_utils import LogUtilsclass DataUtils:    @staticmethod    def get_yaml_data(path, file_name):        file_path = BASE_DIR + os.sep + 'datas' + os.sep + path + os.sep + file_name        # print(file_path)        with open(file_path, 'r', encoding='UTF-8') as f:            data = yaml.safe_load(f)        return data    @staticmethod    def set_data(data, path, filename):        file_path = BASE_DIR + os.sep + 'datas' + os.sep + path + os.sep + filename        with open(file_path, 'w', encoding='UTF-8') as f:            yaml.dump(data, f, allow_unicode=True, encoding='UTF-8')    @staticmethod    def get_json_data(path, file_name):        file_path = BASE_DIR + os.sep + 'datas' + os.sep + path + os.sep + file_name        # print(file_path)        with open(file_path, 'r', encoding='UTF-8') as f:            data = json.load(f)            return data    @staticmethod    def json_to_yaml(path, file_name):        file_path = BASE_DIR + os.sep + 'datas' + os.sep + path + os.sep + file_name        # print(file_path)        with open(file_path, 'r', encoding='UTF-8') as f:            data = json.load(f)            DataUtils.set_data(data, 'alarm_center_api_data' + os.sep + 'ck_es_data', 'get_alarm_infos_data.yaml')            return dataif __name__ == '__main__':    # data = DataUtils.json_to_yaml(str('alarm_center_api_data' + os.sep + 'ck_es_data'), 'get_alarm_infos_data.json')    # data = DataUtils.get_yaml_data(    #     str('alarm_center_api_data' + os.sep + 'ck_es_data' + os.sep + 'get_alarm_infos_data.yaml'))    # print(f'RESULT: \n {json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4)}')    # DataUtils.set_data(data, 'alarm_center_api_data', 'rule_data.yaml')    # data=DataUtils.get_json_data('iot_rule_enigne_data',"create_data.json")    # DataUtils.set_data(data,'iot_rule_enigne_data','create_data_01单测点越限.yaml')    # print(data)    print(DataUtils.get_yaml_data('iot_rule_enigne_data', 'create_data_01单测点越限.yaml'))