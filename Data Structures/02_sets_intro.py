# Create a set using curly brackets
s1 = {1, 2, 3}

# Create a set using the set() constructor
s2 = set([1, 2, 3, 4])

# Print out sets
print(f"Set s1: {s1}")
print(f"Set s2: {s2}")





# Create two new sets
names1 = set(["Glory", "Tony", "Joel", "Dennis"])
names2 = set(["Morgan", "Joel", "Tony", "Emmanuel", "Diego"])

# Create a union of two sets using the union() method
names_union = names1.union(names2)

# Create a union of two sets using the | operator
names_union = names1 | names2

# Print out the resulting union
print(names_union)





# Intersection of two sets using the intersection() method
names_intersection = names1.intersection(names2)

# Intersection of two sets using the & operator
names_intersection = names1 & names2

# Print out the resulting intersection
print(names_intersection)





# Create a set of all the names present in names1 but absent in names2 with the difference() method
names_difference = names1.difference(names2)

# Create a set of all the names present in names1 but absent in names2 with the - operator
names_difference = names1 - names2

# Print out the resulting difference
print(names_difference)