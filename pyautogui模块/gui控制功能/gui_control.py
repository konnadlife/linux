import pyautogui
# 由于鼠标自动操作非常迅速而且程序比较难关闭
# 所以有两个方法针对该情况

# 1.自动防故障
pyautogui.FAILSAFE = False
# 该项默认为True，这个功能意味着：
# 当鼠标的指针在屏幕的最左上方，程序会报错，目的是为了防止程序无法停止

# 2.停顿功能
pyautogui.PAUSE = 1
# 意味着所有pyautogui的指令都要暂停1秒，其他指令不会停顿

