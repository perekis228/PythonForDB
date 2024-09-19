from PIL import Image, ImageDraw, ImageFont

for i in range(1, 4):
    img = Image.new('RGB', (100, 100), 'blue')
    pencil = ImageDraw.Draw(img)
    pencil.rectangle((5, 5, 95, 95), fill ='white')
    font = ImageFont.truetype("FreeMono.ttf", 40)
    pencil.text((38, 30), text=str(i), font=font, fill='red')
    img.show()
    img.save(f'Photos/square{i}.png')