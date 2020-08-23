import unicornhathd

print(""" I am currently busy

Please wait until this turns green to make contact.

Thank you.
""")

unicornhathd.brightness(.6)

unicornhathd.clear()

for xValue in range(0,15):
    for yValue in range(0,15):
        unicornhathd.set_pixel(xValue,yValue,255,0,0)

unicornhathd.brightness(.6)

try:
    while True:
        unicornhathd.show()

except KeyboardInterrupt:
    print("error")
    unicornhathd.off()
