import pyautogui

# 获取屏幕截图
# im = pyautogui.screenshot()：返回屏幕的截图，是一个Pillow的image对象
# im.getpixel((500, 500))：返回im对象上，（500，500）这一点像素的颜色，是一个RGB元组
# pyautogui.pixelMatchesColor(500,500,(12,120,400)) ：是一个对比函数，对比的是屏幕上（500，500）这一点像素的颜色，与所给的元素是否相同；
im = pyautogui.screenshot()
im.save('./screenshot.png')
rgb_1 = im.getpixel((1500, 540))
print(rgb_1)
print(pyautogui.pixelMatchesColor(1600, 580, rgb_1))

# 识别图像
# 首先，我们需要先获得一个屏幕快照，例如我们想要点赞，
# 我们就先把大拇指的图片保存下来；然后使用函数：
# locateOnScreen(‘zan.png’) ，如果可以找到图片，则返回图片的位置，
# 如：Box(left=25, top=703, width=22, height=22)；
# pyautogui.center((left, top, width, height)) 返回指定位置的中心点；
# 如果找不到图片，则返回None;
# 如果，屏幕上有多处图片可以匹配，
# 则需要使用locateAllOnScreen(‘zan.png’) ，
# 如果匹配到多个值，则返回一个list，参考如下：
win_position = pyautogui.locateOnScreen('./windows10.jpg')
print(win_position)
print(pyautogui.center(win_position))
center_position = pyautogui.center(win_position)
pyautogui.moveTo(center_position, duration=2)
pyautogui.click(duration=1)