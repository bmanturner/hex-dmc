from PIL import Image
from collections import defaultdict
from operator import itemgetter
import hex_dmc
import time

img = Image.open('file.jpg')
img.thumbnail((200,200))

by_color = defaultdict(int)

for pixel in img.getdata():
	by_color[pixel] += 1

color_freq = sorted(by_color.iteritems(), key=itemgetter(1,0), reverse=True)

dmc_freq = defaultdict(int)
start = time.clock()
for x in range(len(color_freq)):
	code, desc, close = hex_dmc.rgbToDMC(list(color_freq[x][0]))
	dmc_freq[code] += 1
	print close
end = time.clock()
print end - start

dmc_freq = sorted(dmc_freq.iteritems(), key=itemgetter(1,0), reverse=True)

for x in range(10):
	print dmc_freq[x]