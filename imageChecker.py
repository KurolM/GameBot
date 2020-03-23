from PIL import Image


def check_image():
    x = 47
    y = 7

    im = Image.open('Enter_game.jpg')  # Can be many different formats.
    pix = im.load()

    magic_pixel = pix[x, y]
    valid_colors = [
        (116, 94, 254),
        (115, 95, 252)
    ]

    print(im.size)  # Get the width and height of the image for iterating over
    print(pix[x, y])  # Get the RGBA Value of the a pixel of an image

    im.save('Enter_game.jpg')  # Save the modified pixels as .png

    """If the 47, 7 pixel is (116, 94, 254) coloured"""
    if magic_pixel in valid_colors:
        print("utevo lux")
    else:
        print("not yet")


def selected_pixel_in_color_list(image_file, x, y, color_list):
    im = Image.open(image_file)
    image_pixels = im.load()
    selected_pixel = image_pixels[x, y]

    return selected_pixel in color_list
