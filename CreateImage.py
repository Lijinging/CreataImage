def createImg(width=1920, height=1080, back=(255,255,255), colors=[(255,255,255), (0,0,0)], filename="img.png", type="png"):
    import Image
    import ImageDraw
    image = Image.new('RGB', (width, height), back)
    draw = ImageDraw.Draw(image)
    length = len(colors)
    for y in range(height):
        index = y % length
        for x in range(width):
            draw.point((x, y), fill=colors[index])
            index = (index + 1) % length
    image.save(filename, type)


createImg()