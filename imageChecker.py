import pyautogui
from PIL import Image


def check_image():

    """PIL DOC `This is a lazy operation; this function identifies the file,
     but the file remains open and the actual image data is not read from the file until you try to process the data`"""
    im = Image.open('mana.jpg')  # Can be many different formats.
    pix = im.load()

    x = 47
    y = 7

    magic_pixel = pix[x, y]
    mana_color_grey = [
        (116, 94, 254),
        (115, 95, 252)
    ]

    print(im.size)  # Get the width and height of the image for iterating over
    print(magic_pixel)  # Get the RGBA Value of the a pixel of an image

    im.save('mana.jpg')  # Save the modified pixels as .png

    """If the 47, 7 pixel is (116, 94, 254) coloured"""
    if magic_pixel in mana_color_grey:
        pyautogui.press('f1', 0.05)
        pyautogui.press('enter')
    else:
        print("not yet")


def selected_pixel_in_color_list(image_file, x, y, color_list):
    im = Image.open(image_file)
    image_pixels = im.load()
    selected_pixel = image_pixels[x, y]

    return selected_pixel in color_list
