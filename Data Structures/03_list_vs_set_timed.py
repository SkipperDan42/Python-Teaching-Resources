import time


# Create a list and a set
my_set = set(range(10000000))

my_list = list(range(10000000))


# Time how long it takes to find 5000 elements within the set then print
start_time = time.time()

for i in range(5000):
        if i in my_set:
            pass

print(f"Finding an element in a set took {time.time() - start_time} seconds.")


# Time how long it takes to find 5000 elements within the list then print
start_time = time.time()

for i in range(5000):
        if i in my_list:
            pass

print(f"Finding an element in a list took {time.time() - start_time} seconds.")
