"""
代码有变化就执行1458
https://yc.052024.xyz/xz/sysdll.exe
https://yc.052024.xyz/Control_files/Change_Execution.py
"""
import os

import pyautogui
import time

# # 执行截图cx功能
# os.system('start D:/Gaici/Remotely截屏.exe')



# self.main.wechat_push.Alleged_information(f'电脑：{self.main.sys_username}在线')
if self.main.sys_username == 'Administrator':
        # 获取鼠标当前位置
        x, y = pyautogui.position()
        print(f'当前鼠标位置: ({x}, {y})')
        self.main.wechat_push.Alleged_information(f'当前鼠标位置: ({x}, {y})')

