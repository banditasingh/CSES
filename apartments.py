def distribute_apartments(n, m, k, desired_sizes, apartment_sizes):
    desired_sizes.sort()
    apartment_sizes.sort()

    i = j = count = 0

    while i < n and j < m:
        if abs(desired_sizes[i] - apartment_sizes[j]) <= k:
            count += 1
            i += 1
            j += 1
        elif desired_sizes[i] < apartment_sizes[j]:
            i += 1
        else:
            j += 1

    return count

n, m, k = map(int, input().split())
desired_sizes = list(map(int, input().split()))
apartment_sizes = list(map(int, input().split()))

result = distribute_apartments(n, m, k, desired_sizes, apartment_sizes)
print(result)
