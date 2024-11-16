# Explanation
print("\nSearching in a list:")
print("- Use the `in` keyword to check if a value exists in the list.")
print("- Use the `index(value)` method to find the index of a value (throws an error if not found).")

# Example code
my_list = [5, 10, 15, 20, 25]  # Initial list
print("\nInitial list:", my_list)

# Check if a value exists
value_to_find = 15
if value_to_find in my_list:
    print(f"{value_to_find} is in the list.")
else:
    print(f"{value_to_find} is not in the list.")

# Find the index of a value
try:
    index = my_list.index(20)
    print(f"Index of 20 is {index}.")
except ValueError:
    print("Value not found in the list.")
    print("Value not found in the list.")
