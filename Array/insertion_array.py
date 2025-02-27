sifat = [1, 2, 3, 4]

# Print the array before insertion
print("Array before insertion:")
for i in range(len(sifat)):
    print(f"sifat {i} = {sifat[i]}")

# Insert new elements and modify the existing ones
for i in range(len(sifat)):
    sifat[i] = i + 1  # Modify the existing element

# Now append new elements
for i in range(len(sifat)):
    sifat.append(i)

# Print the array after modification and insertion
print("Array after the Insertion:")
for i in range(len(sifat)):
    print(f"sifat {i} = {sifat[i]}")
