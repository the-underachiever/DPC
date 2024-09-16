def find_subarrays(arr):
    n = len(arr)
    cumulative_sum = 0
    sum_indices = {0: -1}
    result = []

    for i in range(n):
        cumulative_sum += arr[i]
        if cumulative_sum in sum_indices:
            for j in range(sum_indices[cumulative_sum] + 1, i + 1):
                result.append((sum_indices[cumulative_sum] + 1, j))
        if cumulative_sum not in sum_indices:
            sum_indices[cumulative_sum] = i

    return result

print(find_subarrays([4, -1, -3, 1, 2, -1]))
print(find_subarrays([1, 2, 3, 4]))
print(find_subarrays([0, 0, 0]))
print(find_subarrays([-3, 1, 2, -3, 4, 0]))
X = find_subarrays([1, -1, 2, -2, 3, -3] * 10**4)
