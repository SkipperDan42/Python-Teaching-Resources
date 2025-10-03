
# Now we'll attempt to find the most popular baby names of 2024
# that also happen to be the names of Beanie Babies

# While we could cross reference two lists, it is far quicker
# to use sets in this instance (and we don't care about order)
beanie_baby_names = set()
bb_file = open("BeanieBabies.csv", "r")

# As before we will read the file using a for loop
# - however we will adjust this to enumerate each line
for i, line in enumerate(bb_file):
	stripped_line = line.replace("\n","")
	split_line = stripped_line.split(" the ")

	# enumerating the loop allows us to ignore the header
	if i != 0:
		beanie_baby_names.add(split_line[0])

bb_file.close()



# We will repeat this for the list of baby names
popular_baby_names = set()
gbn_file = open("girl_boy_names_2023.csv", "r")

# Enumerating a for loop again
# - notice that this csv has multiple columns
for i, line in enumerate(gbn_file):
	stripped_line = line.replace("\n","")
	split_line = stripped_line.split(",")
	if i != 0:
		popular_baby_names.add(split_line[1])
		popular_baby_names.add(split_line[2])

bb_file.close()


# Now we find the intersection of both sets
names_union = beanie_baby_names.intersection(popular_baby_names)

# For readability, we can print this one name at a time
for name in names_union:
	print(name)
