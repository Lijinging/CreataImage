import Image

distortion = 0

def createImg(darkImg, brightImg, outImg):
    dark = Image.open(darkImg, 'r').convert('LA').split()[0]
    bright = Image.open(brightImg, 'r').convert('LA').split()[0]
    assert dark.size == bright.size

    def conv(c1, c2):
        c = round(255 * c1 / (255 + c1 - c2)) if 255 + c1 - c2 != 0 else 0
        alpha = 255 + c1 - c2 if 255 + c1 - c2 <= 255 else 255
        global distortion
        if 255 + c1 - c2 > 255:
            distortion += 1
        return (int(c), alpha)

    newdata = list(map(conv, dark.getdata(), bright.getdata()))
    print('distortion:%.2f%%' % (distortion / len(newdata) * 100))

    img = Image.new('LA', dark.size)
    img.putdata(newdata)

    img.save(outImg, "PNG")

createImg("Image/dark.jpg", "Image/bright.jpg", "Image/new.png")
