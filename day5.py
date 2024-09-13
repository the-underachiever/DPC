def find_leaders(arr):
    leaders = []
    max_right = arr[-1]
    leaders.append(max_right)
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > max_right:
            max_right = arr[i]
            leaders.append(max_right)
    return leaders[::-1]

arr = [1, 2, 3, 4, 0]
print("Test Case 1:", find_leaders(arr))

arr = [7, 10, 4, 10, 6, 5, 2]
print("Test Case 2:", find_leaders(arr))

arr = [5]
print("Test Case 3:", find_leaders(arr))

arr = [100, 50, 20, 10]
print("Test Case 4:", find_leaders(arr))

arr = list(range(1, 1000001))
print("Test Case 5:", find_leaders(arr))
