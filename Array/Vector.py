# Declare a list (vector equivalent)
vec = []

# Adding elements to the list
vec.append(10)  # Adds 10 at the end
vec.append(20)  # Adds 20 at the end
vec.append(30)  # Adds 30 at the end

# Printing elements of the list
print("Elements in the list:")
for element in vec:
    print(element, end=" ")
print()

# Removing last element
vec.pop()  # Removes the last element (30)

# Printing elements after removing
print("Elements after popping one:")
for element in vec:
    print(element, end=" ")
print()

# Accessing the first element using index
print("First element:", vec[0])
