from PIL import Image, ImageDraw, ImageFont, ImageFilter

with Image.open('Photos/Cat.jpg') as img:
    watermark = Image.open('Photos/Water.jpg')
    watermark = watermark.convert("L")
    watermark = watermark.point(lambda x: 255 if x > 50 else 0)
    watermark = watermark.resize((watermark.width // 8, watermark.height // 8))
    watermark = watermark.filter(ImageFilter.CONTOUR)
    watermark = watermark.point(lambda x: 0 if x == 255 else 255)
    img.paste(watermark, (50, 50), watermark)

    drawing = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeMono.ttf", 60)
    drawing.text((0, 0), 'WaterMark', fill=(3, 8, 12), font=font)

    img.show()
    img.save('Photos/CatWaterMark.jpg')