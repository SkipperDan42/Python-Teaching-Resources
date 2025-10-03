import os
# Load in Welsh_Counties file





# Will always work:
wc_file = open("/Users/dan/Documents/Python/Teaching Resources/ReadWrite/Welsh_Counties.txt", "r")

# Should work in an IDE
# - but may not in Terminal or with symbolic file paths:
wc_file = open("Welsh_Counties.txt", "r")

# Should always work (so long as file in same directory)
# - will require importing 'os'
# - parts of this will be explained later in the course
wc_file = open(
				os.path.join(os.path.dirname(__file__), 
				"Welsh_Counties.txt"), "r")






# Read the file (i.e. convert from encoded data to text)
# and close afterward (important for efficiency and safety)
welsh_counties = wc_file.read()
wc_file.close()

# Print the data read from the file
print(welsh_counties)

# Check the data-type of the data read into memory
print(type(welsh_counties))





# Reopen the file and read in using readline(), then close
wc_file = open("Welsh_Counties.txt", "r")
welsh_counties_list = wc_file.readline()
wc_file.close()

# Print the list
print(welsh_counties_list)





# Now repeat the above using readlines() instead
wc_file = open("Welsh_Counties.txt", "r")
welsh_counties_list = wc_file.readlines()
wc_file.close()
print(welsh_counties_list)





# Why does every entry in the list have a '\n'?





# We can remove this artifact as it is unnecessary of our list
welsh_counties_list = []
wc_file = open("Welsh_Counties.txt", "r")

# This for loop has the same functionality as readlines()
# but allows us to modify each line as it is read
for line in wc_file:
	stripped_line = line.replace("\n","")
	welsh_counties_list.append(stripped_line)

wc_file.close()
print(welsh_counties_list)
