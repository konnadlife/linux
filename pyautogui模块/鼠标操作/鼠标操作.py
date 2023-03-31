import pyautogui
# 安全操作
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.5

# 控制鼠标移动：
# 1.获得屏幕分辨率
print(pyautogui.size())     # Size(width=1920, height=1080)
width, height = pyautogui.size()
print(width, height)        # 1920 1080

# 2.移动鼠标
# 移动到指定位置,duration是设置移动时间
pyautogui.moveTo(960, 540, duration=1)
# 按方向移动,表示向右移动-192px，向下移动108px
pyautogui.moveRel(-192, 108, duration=1)

# 3.获取鼠标位置
print(pyautogui.position())  # Point(x=768, y=648)

# 控制鼠标点击:
pyautogui.click(10, 10, duration=1)   # 鼠标点击指定位置，默认左键
# pyautogui.click(10, 10, button='left')  # 单击左键
# pyautogui.click(1000, 300, button='right')  # 单击右键
# pyautogui.click(1000, 300, button='middle')  # 单击中间

# pyautogui.doubleClick(10, 10, duration=1)  # 左键双击
# pyautogui.rightClick(10, 10, duration=1)   # 右键双击
# pyautogui.middleClick(10, 10, duration=1)  # 中键双击

# pyautogui.mouseDown()    # 鼠标按下
# pyautogui.mouseUp()      # 鼠标释放

# 控制鼠标拖动
pyautogui.dragTo(960, 540, duration=1)
pyautogui.dragRel(-196, 108, duration=1)

# 控制鼠标滚动,参数表示向上滚动的单位数
pyautogui.scroll(300)
