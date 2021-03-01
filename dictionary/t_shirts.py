wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothing, colors in wardrobe.items():
	for color in colors:
		print("{} {}".format(color, clothing)) 
