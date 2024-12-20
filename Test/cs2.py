import subprocess

# 要执行的命令，这里以获取系统信息（systeminfo）为例
command = "systeminfo"

# 使用run函数执行命令，通过shell=True在系统的shell中执行，需要注意安全问题
try:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"命令执行失败，错误信息: {result.stderr}")
except Exception as e:
    print(f"发生错误: {e}")