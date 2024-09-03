import requests



def get_web(num_url):
    # 发送GET请求
    response = requests.get(num_url)
    # 检查请求是否成功
    if response.status_code == 200:
        # 获取响应内容
        content = response.text
        print(content)
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
Current_version = '1.0'     # 当前版本

if __name__ == '__main__':
    yc_kz_xx = get_web(url)

    ...
