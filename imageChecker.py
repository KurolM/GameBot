from PIL import Image


def check_image():
    x = 47
    y = 7
    im = Image.open('Enter_game.jpg')  # Can be many different formats.
    pix = im.load()

    print(im.size)  # Get the width and height of the image for iterating over
    print(pix[x, y])  # Get the RGBA Value of the a pixel of an image

    im.save('Enter_game.jpg')  # Save the modified pixels as .png

    """If the 47, 7 pixel is (116, 94, 254) coloured"""
    if pix[47, 7] == (116, 94, 254) or pix[47, 7] == (115, 95, 252):
        print("utevo lux")
    else:
        print("not yet")
