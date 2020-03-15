import cv2, pyautogui
import numpy as np
from pywinauto.application import Application
from ctypes import windll
from PIL import Image, ImageGrab
from datetime import datetime, timedelta


"""To load the bbox coords properly"""
user32 = windll.user32
user32.SetProcessDPIAware()

app = Application().start("RealestaDX9.exe")
cv2.waitKey(1000)
pyautogui.click(x=148, y=757)
cv2.waitKey(500)
pyautogui.write('6991385', 0.05)
pyautogui.press('tab')
cv2.waitKey(500)
pyautogui.write('gxan7xv2', 0.05)
pyautogui.press('enter')
cv2.waitKey(1000)
pyautogui.press('enter')
cv2.waitKey(2000)

""" Grab the mana bar"""
# mana box grabber (100% mana) // 1920 / 1080 - resolution of Dell Precision laptop
mana_box_100 = ImageGrab.grab(bbox=(1723, 246, 1836, 260))
mana_box_100_np = np.array(mana_box_100)
frame_mana_box_100 = cv2.cvtColor(mana_box_100_np, cv2.COLOR_BGR2RGB)

hp_box_100 = ImageGrab.grab(bbox=(1723, 230, 1836, 244))
hp_box_100_np = np.array(hp_box_100)
frame_hp_box_100 = cv2.cvtColor(hp_box_100_np, cv2.COLOR_BGR2RGB)

#showImg = cv2.imshow("Hp", frame_hp_box_100)

"""Write the mana bar"""
#showImg = cv2.imshow("Mana", frame_mana_box_100)
cv2.imwrite("mana.jpg", frame_mana_box_100)
cv2.waitKey(0)
cv2.destroyAllWindows()

x = 47
y = 7

im = Image.open('Enter_game.jpg')  # Can be many different formats.
pix = im.load()

print(im.size)  # Get the width and height of the image for iterating over
print(pix[x, y])  # Get the RGBA Value of the a pixel of an image

"""If the 47, 7 pixel is (116, 94, 254) coloured"""
if pix[47, 7] == (116, 94, 254) or pix[47, 7] == (115, 95, 252) or pix[47, 7] == (13, 70, 219):
    pyautogui.write("utevo lux", 0.05)
    pyautogui.press('enter')
    print("utevo lux")
else:
    pyautogui.write("a", 0.05)
    print("not enough mana")


# INTERVAL = timedelta(seconds=1)
# last_checked = datetime.now() - INTERVAL
#
# while True:
#     now = datetime.now()
#     if last_checked <= (now - INTERVAL):
#         if not if_active():
#             break
#         last_checked = now
#
#     # do your thing here
#     pass