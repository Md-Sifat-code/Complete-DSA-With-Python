def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_side = arr[:mid]
        right_side = arr[mid:]

        # Recursive calls to divide the array into halves
        merge_sort(left_side)
        merge_sort(right_side)

        # Merge the sorted halves back into arr
        i = j = k = 0
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                arr[k] = left_side[i]
                i += 1
            else:
                arr[k] = right_side[j]
                j += 1
            k += 1

        # If there are remaining elements in left_side
        while i < len(left_side):
            arr[k] = left_side[i]
            i += 1
            k += 1

        # If there are remaining elements in right_side
        while j < len(right_side):
            arr[k] = right_side[j]
            j += 1
            k += 1

    # No need to return arr, as it is modified in place


arr = [27, 32, 1, 45, 3, 6, 7, 8, 10]
merge_sort(arr)
print(arr)  # Print the sorted array
