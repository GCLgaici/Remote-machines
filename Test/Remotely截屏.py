import pyautogui
import time


while True:
    # 截取全屏
    screenshot = pyautogui.screenshot()

    # 保存截图
    screenshot.save("D:/Gaici/screenshot.png")
    time.sleep(0.8)
