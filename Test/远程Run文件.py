import pyautogui

# 定义要截取的区域 (x, y, width, height)
region = (0, 0, 800, 600)  # 从左上角 (0, 0) 开始，宽 800 高 600

# 截取特定区域
screenshot = pyautogui.screenshot(region=region)

# 保存截图到文件
screenshot.save("D:/Gaici/screenshot_region.png")
print("区域截图已保存为 screenshot_region.png")

