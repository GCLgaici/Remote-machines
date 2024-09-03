import requests

# 目标URL
url = 'https://yc.052024.xyz/Web/Background_detection.txt'

# 发送GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 获取响应内容
    content = response.text
    print(content)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
