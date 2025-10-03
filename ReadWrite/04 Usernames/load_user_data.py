# These are all fun examples, but what are the practical
# uses of these methods?

# If we had some application that required user data,
# instead of storing that user data within the code
# (a terrible idea) - we could load it from file each
# time we open the program...
user_data = list()
user_file = open("username.csv", "r")

# Again enumerating a for loop to ditch the headers
for i, line in enumerate(user_file):
	stripped_line = line.replace("\n","")
	split_line = stripped_line.split(";")

	# Individually creating a dictionary for each user
	# and adding them to a list of users
	if i != 0:
		user = dict()
		user["username"] 	= split_line[0]
		user["id"] 			= split_line[1]
		user["first name"] 	= split_line[2]
		user["surname"] 	= split_line[3]
		user_data.append(user)

user_file.close()

# Print all users
for user in user_data:
	print(user)



# Now we will try adding a new user to the list,
# to do this we will create a new dictionary
new_user = {"username": "adams42", "id": "1978", 
			"first name": "Douglas", "surname": "Adams"}
user_data.append(new_user)





# We can write this new user to file using a very similar
# method to that which we've used for reading

# Notice that this is a new file, Python can create files dynamically!
# Also it's never a good idea to overwrite files (there's no undo with Python!)
user_file = open("new_username.csv", "w")

# We will have to rewrite the header manually, as we have not stored it.
user_file.write("Username;Identifier;First name;Last name\n")

# Now we loop through the users, and write each element of the dictionary
# while also specifying the semicolons between each, and the escape character.
for user in user_data:
	user_file.write(user["username"] + ";"
					+ user["id"] + ";"
					+ user["first name"] + ";"
					+ user["surname"] + "\n")

user_file.close()
