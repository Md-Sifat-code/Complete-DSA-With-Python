# Function to perform binary search on a sorted list
def binary_search(arr, target):
    # Initialize two pointers for the start and end of the list
    low = 0
    high = len(arr) - 1

    # Continue searching while low pointer is less than or equal to high pointer
    while low <= high:
        # Calculate the middle index (using // for integer division)
        mid = low + (high - low) // 2

        # If the middle element matches the target, return the index
        if arr[mid] == target:
            return mid

        # If the middle element is less than the target,
        # move the low pointer to mid + 1 (search right half)
        elif arr[mid] < target:
            low = mid + 1

        # If the middle element is greater than the target,
        # move the high pointer to mid - 1 (search left half)
        else:
            high = mid - 1

    # If we exit the loop, the target is not in the list
    return -1


# Main block to demonstrate binary search
if __name__ == "__main__":
    # Example sorted list to search in
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    target = 11  # Element we are searching for

    # Perform binary search and capture the result
    result = binary_search(arr, target)

    # Output the result based on whether the target was found
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the list")
