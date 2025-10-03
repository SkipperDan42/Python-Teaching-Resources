# Create an empty list using square brackets
l1 = []

# Create a four-element list using square brackets
l2 = [1, 2, "3", 4]  # Note that this lists contains two different data types: integers and strings

# Create an empty list using the list() constructor
l3 = list()

# Create a three-element list from a tuple using the list() constructor
# We will talk about tuples later in the tutorial
l4 = list((1, 2, 3))





# Print out lists
print(f"List l1: {l1}")
print(f"List l2: {l2}")
print(f"List l3: {l3}")
print(f"List l4: {l4}")





# Print out the first element of list l2
print(f"The first element of the list l2 is {l2[0]}.")
print()

# Print out the third element of list l4
print(f"The third element of the list l4 is {l4[2]}.")





# Assign the third and the fourth elements of l2 to a new list
l5 = l2[2:]

# Print out the resulting list
print(l5)





# The : is used to slice a list, we do not have to include the start/end index, as shown above
print(f"List l2: {l2}")

# Access the second and the third elements of list l2 (these are the indices 1 and 2)
print(f"Second and third elements of list l2: {l2[1:3]}")





# Append a new element to the list l1
l1.append(5)

# Print the modified list
print("Appended 5 to the list l1:")
print(l1)

# Remove element 5 from the list l1
l1.remove(5)

# Print the modified list
print("Removed element 5 from the list l1:")
print(l1)





# Print the original list l2
print("Original l2:")
print(l2)

# Change value at index 2 (third element) in l2
l2[2] = 5

# Print the modified list l2
print("Modified l2:")
print(l2)