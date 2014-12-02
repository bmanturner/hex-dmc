from math import sqrt

# Calculates color difference based on weighted Euclidean distance
def ColorDiff(rgb1, rgb2):
	rmean = abs((rgb1[0]-rgb2[0])*0.5)
	r = abs(rgb1[0] - rgb2[0])
	g = abs(rgb1[1] - rgb2[1])
	b = abs(rgb1[2] - rgb2[2])
	return sqrt((((2+(rmean/256))*r*r)) + 4*g*g + (((2+((255-rmean)/256))*b*b)));

# Convert user hex into RGB values
while True:
	try:
		user_hex = raw_input('Enter hex color to convert: ')
		user_hex = user_hex.replace('#','')
		r = int("0x%s%s" % (user_hex[0],user_hex[1]), 16)
		g = int("0x%s%s" % (user_hex[2],user_hex[3]), 16)
		b = int("0x%s%s" % (user_hex[4],user_hex[5]), 16)
		user_rgb = [r,g,b]
		break
	except ValueError:
		print "Hex colorcode is invalid. Try again..."

# Load DMC color chart (source: http://www.camelia.sk/dmc_1.htm)
dmc_file = open("est_dmc_hex.txt", "r")
dmc_list = []
for line in dmc_file:
	dmc_list.append(line.rstrip())
dmc_file.close()

# Loop through color chart and find nearest DMC thread color
res = [1000, '', '', '']
for x in range(0, len(dmc_list), 3):
	r = int("0x%s%s" % (dmc_list[x+2][0],dmc_list[x+2][1]), 16)
	g = int("0x%s%s" % (dmc_list[x+2][2],dmc_list[x+2][3]), 16)
	b = int("0x%s%s" % (dmc_list[x+2][4],dmc_list[x+2][5]), 16)
	dmc_rgb = [r,g,b]
	diff = ColorDiff(user_rgb,dmc_rgb) 
	if diff < res[0]:
		res[0] = diff
		res[1] = dmc_list[x]
		res[2] = dmc_list[x+1]

print "The closest DMC thread to #%s is '[%s] - %s'" % (user_hex, res[1], res[2])
print "Closeness (lower is closer): %s" % (res[0])
