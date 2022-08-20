import pyautogui

# i = pyautogui.locateOnScreen('7.png')
# q = pyautogui.center(i)

# num7= pyautogui.locateCenterOnScreen('7.png')
# pyautogui.click(num7)

# print(pyautogui.position())
pyautogui.screenshot('1.png',region=(1084,405,30,30))

num1= pyautogui.locateCenterOnScreen('1.png')
pyautogui.click(num1)