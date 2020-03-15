from PIL import ImageGrab
import numpy as np
import cv2
from ctypes import windll


def picture_of_mana():
    """This part of code is for proper image capturing"""
    user32 = windll.user32
    user32.SetProcessDPIAware()

    # mana box grabber (100% mana) // 1920 / 1080 - resolution of Dell Precision laptop
    mana_box_100 = ImageGrab.grab(bbox=(1723, 246, 1836, 260))
    mana_box_100_np = np.array(mana_box_100)
    frame_mana_box_100 = cv2.cvtColor(mana_box_100_np, cv2.COLOR_BGR2RGB)

    #showImg = cv2.imshow("Mana", frame_mana_box_100)
    cv2.imwrite("mana.jpg", frame_mana_box_100)
    cv2.waitKey(0)
    cv2.destroyAllWindows()