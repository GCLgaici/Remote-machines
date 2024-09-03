import os

import os

# 目标目录
directory = '..'





if __name__ == '__main__':
    # 获取文件列表
    files = os.listdir(directory)
    # 打印文件列表
    for file in files:
        print(file)
