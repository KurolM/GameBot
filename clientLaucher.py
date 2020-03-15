import cv2
import pyautogui
from pywinauto.application import Application
from ctypes import windll
import mana_level
import imageChecker


def run_realesta():
    """Proper image capturing"""
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


if __name__ == "__main__":
    run_realesta()
    cv2.waitKey(5000)
    mana_level.picture_of_mana()
    cv2.waitKey(200)
    imageChecker.check_image()