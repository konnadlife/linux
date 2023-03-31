import pyautogui

a = pyautogui.alert(text='this is a alert box', title='test')
print(a)
# 点击确定后返回值为ok

b = pyautogui.confirm('choose one', buttons=['A', 'B', 'C'])
print(b)
# 点击B选项，返回值为‘B’
