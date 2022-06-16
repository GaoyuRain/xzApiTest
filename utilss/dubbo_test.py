"""
author :admin
Date : 2022/01/27
Description :
"""
import re
import telnetlib
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

'''
方法调用案例：
conn = InvokeDubboApi('127.0.0.1:88888')
data = {
    'dubbo_service': 'xxx.xxx.xx.xxxx.xxxx.xxxx.Service',
    'dubbo_method': 'xxxxx',
    'parameters': ({"age":41,"name":"tom"},"sh",564645,)
    }
invoke = json.loads(conn.invoke_dubbo_api(data))
conn.logout()
'''


class TelnetClient(object):
    """通过telnet连接dubbo服务, 执行shell命令, 可用来调用dubbo接口
    """

    def __init__(self, server_host, server_port):
        self.conn = telnetlib.Telnet()
        self.server_host = server_host
        self.server_port = server_port

    # telnet登录主机
    def connect_dubbo(self):
        try:
            logging.info("telent连接dubbo服务端: telnet {} {} ……".format(self.server_host, self.server_port))
            self.conn.open(self.server_host, port=self.server_port)
            return True
        except Exception as e:
            logging.info('连接失败, 原因是: {}'.format(str(e)))
            return False

    # 执行传过来的命令，并输出其执行结果
    def execute_command(self, command):
        # 执行命令
        cmd = 'invoke {}\n'.format(command).encode("utf-8")
        self.conn.write(cmd)
        # 初始化调用次数
        invoke_count = 0
        # 若调用无返回时，记录次数并重试
        result = self.conn.read_very_eager().decode(encoding='utf-8').split('\r\n')[0]
        while result == '':
            time.sleep(1)
            result = self.conn.read_very_eager().decode(encoding='utf-8').split('\r\n')[0]
            invoke_count += 1
            if invoke_count >= 5:
                logging.info("调用dubbo接口超过五次，调用失败")
                return '调用dubbo接口失败'
        return result

    # 退出telnet
    def logout_host(self):
        self.conn.write(b"exit\n")
        logging.info("登出成功")


class InvokeDubboApi(object):

    def __init__(self, content):
        # 解析dubbo部署的ip和port
        try:
            dubboaddrre = re.compile(r"([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+)", re.I)
            result = dubboaddrre.search(str(content)).group()
            server_host = result.split(":")[0]
            server_port = result.split(":")[1]
            logging.info("获取到dubbo部署信息" + result)
        except Exception as e:
            raise Exception("获取dubbo部署信息失败：{}".format(e))

        try:
            self.telnet_client = TelnetClient(server_host, server_port)
            self.login_flag = self.telnet_client.connect_dubbo()
        except Exception as e:
            logging.info("invokedubboapi init error" + e)

    # 调用dubbo接口
    def invoke_dubbo_api(self, data):
        cmd = data.get("dubbo_service") + "." + data.get("dubbo_method") + "{}".format(data.get("parameters"))
        logging.info("调用命令是：{}".format(cmd))
        resp = None
        try:
            if self.login_flag:
                result = self.telnet_client.execute_command(cmd)
                logging.info("接口响应是,result={}".format(resp))
                return result
            else:
                logging.info("登陆失败！")
        except Exception as e:
            raise Exception("调用接口异常, 接口响应是result={}, 异常信息为：{}".format(result, e))
        self.logout()

    # 调用多个dubbo接口，注：确保所有接口是同一个ip和port
    def invoke_dubbo_apis(self, datas):
        summary = []
        if isinstance(datas, list):
            for i in range(len(datas)):
                result = self.invoke_dubbo_api(datas[i])
                summary.append({"data": datas[i], "result": result})
            return summary
        else:
            return "请确认入参是list"

    def logout(self):
        self.telnet_client.logout_host()


if __name__ == '__main__':
    data = {
        'dubbo_service': 'xxx.xxx.xx.xxxx.xxxx.xxxxService',
        'dubbo_method': 'delete',
        'parameters': ({"id": "123456789", "mobile": 12456},)
    }
    i = InvokeDubboApi('127.0.0.1:110741')
    i.invoke_dubbo_api(data)
    i.logout()
