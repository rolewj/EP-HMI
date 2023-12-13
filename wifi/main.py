import cmath
import math
import random
import PIL
import PIL.Image

map_w = 12
map = [
	1,1,1,1,1,1,1,1,1,1,1,1,
	1,0,0,0,0,1,0,0,0,0,0,1,
	1,0,0,0,0,1,0,1,1,1,0,1,
	1,0,0,0,0,1,0,1,0,1,0,1,
	1,0,1,1,1,1,0,1,1,1,0,1,
	1,0,0,0,0,0,0,0,0,0,0,1,
	1,0,0,1,0,2,0,0,0,0,0,1,
	1,0,0,1,0,0,0,0,0,1,0,1,
	1,0,0,0,0,0,0,0,0,0,0,1,
	1,1,1,1,1,1,1,1,1,1,1,1
]
map_h = len(map) // map_w

todo = []
sig = []
for i in range(len(map)):
	if map[i] == 2:
		sig.append(1.0)
		todo.append(i)
	else:
		sig.append(0.0)

while len(todo) != 0:
	idx = todo.pop()
	scale = sig[idx]
	x = idx % map_w
	y = idx / map_w
	for iy in [-1,0,1]:
		ty = int(y + iy)
		for ix in [-1,0,1]:
			tx = int(x + ix)
			if tx >= 0 and tx < map_w and ty >= 0 and ty < map_h:
				# dist = (ix * ix + iy * iy) ** 0.5
				# if dist > 0.01:
					tidx = int(ty * map_w + tx)
					s = 0.8 * scale
					if map[tidx] == 1:
						s *= 0.7
					if scale > sig[tidx]:
						sig[tidx] = s
						todo.append(tidx)

newImg1 = PIL.Image.new('RGB', (map_w,map_h))

for y in range(map_h):
	for x in range(map_w):
		idx = y * map_w + x
		if map[idx] == 1:
			newImg1.putpixel((x, y), (0, 0, 0))
		else:
			s = int(sig[idx] * 255)
			newImg1.putpixel((x, y), (255-s, s, 255))

newImg1.save("img.png")
