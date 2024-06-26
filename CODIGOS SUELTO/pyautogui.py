import pyautogui

x,y = pyautogui.position()

w,h = pyautogui.size()

pyautogui.moveTo(484,50,5)
pyautogui.rightClick()
pyautogui.hotkey('ctrol', 'c')
