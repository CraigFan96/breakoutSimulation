from scipy import misc
face = misc.face()
misc.imsave('./gameImages/0.png', face)
face = misc.imread('./gameImages/0.png')
print face.shape, face.dtype
for line in face:
	print line