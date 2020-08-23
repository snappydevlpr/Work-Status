import unicornhathd
import time
from PIL import Image, ImageDraw, ImageFont

def busy_status():

    text = " I am currently available Feel free to enter. :) "

    unicornhathd.clear()
    unicornhathd.brightness(.6)

    for xValue in range(0,15):
        for yValue in range(0,15):
            unicornhathd.set_pixel(xValue,yValue,255,0,0)


    try:
        while True:
            unicornhathd.show()
            time.sleep(.02)
            print_status(text, 255, 0, 0)
    except KeyboardInterrupt:
        print("error")
        unicornhathd.off()

def available_status():
    
    unicornhathd.clear()
    unicornhathd.brightness(.6)

    for xValue in range(0,15):
        for yValue in range(0,15):
            unicornhathd.set_pixel(xValue,yValue,0,255,0)

    try:
        while True:
            unicornhathd.show()

    except KeyboardInterrupt:
        print("error")
        unicornhathd.off()


def print_status(myStatusText, r, g, b):
    TEXT = myStatusText

    FONT = ('/usr/share/fonts/true/type/freefont/FreeSansBold.ttf',12)

    width, height = unicornhathd.get_shape()

    unicornhathd.rotation(90)
    unicornhathd.brightness(.6)

    text_x = 1
    text_y = 2
    
    font_file, font_size = FONT

    font = ImageFont.truetype(font_file. font_size)
    text_widt, text_height = font.getsize(TEXT)

    text_width += width + text_x

    image = Image.new('RGB', (text_width, max(height, text_height)). (0,0,0))

    draw = ImageDraw.Draw(image)

    for scroll in range(text_width - width):
        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x + scroll, y))

                unicornhathd.set_pixel(width-1-x, y,r,g,b)

        unicornhathd.show()

        time.sleep(0.02)

    
busy_status()