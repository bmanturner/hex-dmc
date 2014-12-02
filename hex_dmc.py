from math import sqrt

# Load DMC color chart (source: http://www.camelia.sk/dmc_1.htm)
dmc_file = open("est_dmc_hex.txt", "r")
dmc_list = []
for line in dmc_file:
	dmc_list.append(line.rstrip())
dmc_file.close()

# Calculates color difference based on weighted Euclidean distance
def ColorDiff(rgb1, rgb2):
	rmean = abs((rgb1[0]-rgb2[0])*0.5)
	r = abs(rgb1[0] - rgb2[0])
	g = abs(rgb1[1] - rgb2[1])
	b = abs(rgb1[2] - rgb2[2])
	return sqrt((((2+(rmean/256))*r*r)) + 4*g*g + (((2+((255-rmean)/256))*b*b)));

# Converts hex to RGB list
def hexToRGB(col_hex):
	r = int("0x%s%s" % (col_hex[0],col_hex[1]), 16)
	g = int("0x%s%s" % (col_hex[2],col_hex[3]), 16)
	b = int("0x%s%s" % (col_hex[4],col_hex[5]), 16)
	return [r,g,b]

# Converts rgb to nearest DMC as determined by ColorDiff() by comparing to each DMC
# Optimization required
def rgbToDMC(col_rgb):
	closeness, code, description = 1000,'',''
	for x in range(0, len(dmc_list), 3):
		dmc_rgb = hexToRGB(dmc_list[x+2])
		diff = ColorDiff(col_rgb,dmc_rgb) 
		if diff < closeness:
			closeness = diff
			code = dmc_list[x]
			description = dmc_list[x+1]
	return code, description, closeness


if __name__ == "__main__":
    # Convert user hex into RGB values
	while True:
		try:
			user_hex = raw_input('Enter hex color to convert: ')
			user_hex = user_hex.replace('#','')
			user_rgb = hexToRGB(user_hex)
			break
		except ValueError:
			print "Hex colorcode is invalid. Try again..."

	print rgbToDMC(user_rgb)

