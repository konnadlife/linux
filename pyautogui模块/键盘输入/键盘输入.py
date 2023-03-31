import pyautogui

# pyautogui.keyDown() ： 模拟按键按下；
# pyautogui.keyUp() ： 模拟按键释放；
# pyautogui.press() ： # 就是调用keyDown() & keyUp(),模拟一次按键；
# pyautogui.typewrite('this',0.5) ： 第一参数是输入内容，第二个参数是每个字符间的间隔时间；
# pyautogui.typewrite(['T','h','i','s'])：typewrite 还可以传入单字母的列表

pyautogui.press('Win')

pyautogui.typewrite(['T', 'i', 's', 'left', 'left', 'h'])
# 输出 this

# 快捷键
# 当需要快捷键时，只用上述代码就会麻烦，所以用热键hotkey
pyautogui.hotkey('ctrl', 'c')

