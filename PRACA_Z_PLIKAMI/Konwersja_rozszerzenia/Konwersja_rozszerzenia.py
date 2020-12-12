from PIL import Image

for x in range(4):
	im = Image.open(str(x+1)+'.jpg')
	im.save(str(x+1)+'.png')
