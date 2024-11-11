def selection_sort(arr):
    n = len(arr)

    # Traverse through the entire array
    for i in range(n - 1):
        # Assume the first unsorted element is the minimum
        min_index = i

        # Check the rest of the array for a smaller element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                # Update min_index if a smaller element is found
                min_index = j

        # Swap the minimum element found with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Key Points:
# Time Complexity: O(n²), because of the nested loops.
# Space Complexity: O(1), as it sorts in-place.
# Best Use: Small lists or when memory space is limited.

# Example usage
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))  # Output: [11, 12, 22, 25, 64]
