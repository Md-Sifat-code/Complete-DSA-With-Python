
arr = list(map(int, input("Enter elements: ").split()))
n = len(arr)
print("input :", *arr)

i = 1
while i < n:
    if i > 0 and arr[i] < arr[i - 1]:
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
        print(arr)
        i -= 1
    else:
        i += 1

print("sorted :", *arr)
