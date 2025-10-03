# Create dictionary with duplicate keys
d1 = {"1": 1, "1": 2}
print(d1)

# It will only print one key, although no error was thrown
# If we  try to access this key, then it'll return 2, so the value of the second key
print(d1["1"])

# It is technically possible to create a dictionary, although this dictionary will not support them,
# and will contain only one of the keys





d1 = {}

# Create a two-element dictionary using curly brackets
d2 = {"John": {"Age": 27, "Hometown": "Boston"}, "Rebecca": {"Age": 31, "Hometown": "Chicago"}}
# Note that the above dictionary has a more complex structure as its values are dictionaries themselves!

# Create an empty dictionary using the dict() constructor
d3 = dict()

# Create a two-element dictionary using the dict() constructor
d4 = dict([["one", 1], ["two", 2]])  # Note that we created the dictionary from a list of lists

# Print out dictionaries
print(f"Dictionary d1: {d1}")
print(f"Dictionary d2: {d2}")
print(f"Dictionary d3: {d3}")
print(f"Dictionary d4: {d4}")





# Access the value associated with the key 'John'
print("John's personal data is:")
print(d2["John"])





# Add another name to the dictionary d2
d2["Violet"] = {"Age": 34, "Hometown": "Los Angeles"}

# Print out the modified dictionary
print(d2)