def min_gondolas(n, x, weights):
    weights.sort()
    count = 0
    left = 0
    right = n - 1

    while left <= right:
        if weights[left] + weights[right] <= x:
            left += 1
            right -= 1
        else:
            right -= 1

        count += 1

    return count

n, x = map(int, input().split())
weights = list(map(int, input().split()))

result = min_gondolas(n, x, weights)
print(result)
