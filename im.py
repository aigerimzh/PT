from PIL import Image, ImageDraw
im = Image.open("pil-example-01.png")
rgb_im = im.convert('RGB')
size = rgb_im.size
h, w = size
print(size)
for y in range(0, h):
	for x in range(0, h):
		r, g, b = rgb_im.getpixel((x, y))
		print("%d,%d,%d" % (r,g, b), end = '\t')
	print()

for y in range(0, h):
	for x in range(0, w):
		r, g, b = rgb_im.getpixel((x, y))
		if (r, g, b) == (48, 213, 200):
			print("*", end = '')
		else:
			print(" ", end = '')
	print()