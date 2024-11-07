#What is Linear Search Algorithm?
# ---> Linear Search is a simple searching algorithm used to find an element in a list or array. It works by
# sequentially checking each element of the list until it finds a match or reaches the end of the list.
# If the target element is found, it returns the index of that element; otherwise, it returns -1 indicating that
# the element is not present.


# A Real Life Example about Linear Search Algorithm:--
# ----->> Imagine you’re looking for a book in a stack of books piled on a table. The books are not arranged in any particular
# order, so you start from the top and check each book one by one. As soon as you find the book you’re looking for, you
# stop searching. If you reach the bottom of the pile and still haven’t found it, you conclude that the book isn’t in the stack.


# Time Complexity
# Best Case: O(1) - The element is found at the first position.
# Worst Case: O(n) - The element is either at the last position or not present in the list.
# Average Case: O(n) - On average, half the elements will be checked.



# COde Example:--->

def linear_search(arr, t):
    for index, element in enumerate(arr):
        if element == target:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage
numbers = [10, 25, 30, 45, 50]
target = 45

result = linear_search(numbers, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
