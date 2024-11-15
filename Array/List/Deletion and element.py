# Explanation
print("Deletion in a list:")
print("- Use the `remove(value)` method to delete a specific value.")
print("- Use the `pop(index)` method to remove an element at a specific index.")
print("- Use the `del` keyword to delete an element or the entire list.")

# Example code
my_list = [10, 20, 30, 40, 50]  # Initial list
print("\nInitial list:", my_list)

# Remove a specific value
my_list.remove(30)  # Removes the value 30
print("List after removing 30:", my_list)

# Remove an element by index
removed_element = my_list.pop(2)  # Removes the element at index 2
print(f"List after popping index 2 (removed {removed_element}):", my_list)

# Delete an element using del
del my_list[0]  # Deletes the element at index 0
print("List after deleting the first element:", my_list)
