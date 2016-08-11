from PIL import Image
cat_im = Image.open("images/pikachu.png")
cat_im.show()

cat_list = cat_im.getdata()
new_im = Image.new("RGB", cat_im.size)
new_list = []

for i in cat_list:
	sum = i[0]+i[1]+i[2]
	
	if sum > 546 :
		new_list.append((252, 227, 166))
	elif sum > 364:
		new_list.append((112, 150, 158))
	elif sum > 182:
		new_list.append((217, 26, 33))
	else:
		new_list.append((0, 51, 76))

new_im.putdata(new_list)
new_im.save("pikablu.png")
new_im.show()