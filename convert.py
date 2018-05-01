import cv2
im = cv2.imread("./gameImages/0000/00000.png")
print type(im)


im2 = cv2.imread("./gameImages/0.png")
print type(im2)
x = 1
y = 1
for line in im2:
	if x == 160:
		x = 1
		y += 1
	print x, y
	print line
	x += 1
