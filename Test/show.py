import os
import time
from PIL import Image
import matplotlib.pyplot as plt

# 设置共享文件夹的路径，确保路径格式正确
shared_folder_path = r'\\192.168.1.200\d\Gaici'  # 替换为实际的共享文件夹路径
image_file = os.path.join(shared_folder_path, 'screenshot.png')

plt.ion()  # 开启交互模式
fig, ax = plt.subplots()  # 创建图形和坐标轴

while True:
    if os.path.exists(image_file):  # 检查文件是否存在
        img = Image.open(image_file)  # 读取图片

        ax.clear()  # 清除之前的图像
        ax.imshow(img)  # 显示新读取的图像
        ax.axis('off')  # 关闭坐标轴
        plt.draw()  # 更新图形
    else:
        print(f"文件未找到: {image_file}")

    plt.pause(0.1)  # 设置绘图的刷新时间，这里设置为0.1秒
    time.sleep(0.1)  # 控制循环频率
