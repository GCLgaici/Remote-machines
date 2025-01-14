import json
import requests


def send_Alleged_information(self, access_token, message):  # 发送被控信息
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


