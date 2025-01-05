arr = [1,2,3,4,5,6,7]

for i in range(len(arr)):
    print(f"The memory address of the {i}th element {arr[i]} is {id(i)} ")

# This is a way to find out the memory alocation of an element in an Array.
# In pyton there is nothing called array . We can  use List . List is one type of Dynamic array
# Using the function id() we can get the memory alocation of an element