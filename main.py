import unicornhathd


def busy_status():
    print(""" I am currently busy

    Please wait until this turns green to make contact.

    Thank you.
    """)

    unicornhathd.clear()
    unicornhathd.brightness(.6)

    for xValue in range(0,15):
        for yValue in range(0,15):
            unicornhathd.set_pixel(xValue,yValue,255,0,0)


    try:
        while True:
            unicornhathd.show()

    except KeyboardInterrupt:
        print("error")
        unicornhathd.off()

def available_status():
     print(""" I am currently available
    Feel free to enter. :) """)

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