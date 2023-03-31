import pyautogui

# 密码输入
a = pyautogui.password('enter a password')
print(a)
print(a == '011235')
# 输入密码显示为密文，点击ok后返回输入的值

# 普通输入
b = pyautogui.prompt('enter anything')
print(b)
