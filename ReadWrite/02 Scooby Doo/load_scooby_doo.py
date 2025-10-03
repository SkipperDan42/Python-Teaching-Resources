# We can load files into any data structure we like
# - but it is up to us to provide the code for how
#   this is implemented


scooby_doo_episodes = dict()
sd_file = open("ScoobyDoo.txt", "r")

for line in sd_file:
	# Replace the escape character
	# and split the line at the hash
	stripped_line = line.replace("\n","")
	episode_name_list = stripped_line.split(" - ")

	# Add items to dictionary, using the episode number
	# as a key and the episode name as a value
	scooby_doo_episodes[episode_name_list[0]] = episode_name_list[1]
	
sd_file.close()





# Using the key, get the name of episode 8
print(scooby_doo_episodes["Episode 8"])