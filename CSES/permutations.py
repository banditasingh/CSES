def beautiful_permutation(n):
    if n == 1:
        return [1]

    if n < 4:
        return "NO SOLUTION"

    permutation = list(range(2, n + 1, 2)) + list(range(1, n + 1, 2))

    return permutation

# Get input
n = int(input())

result = beautiful_permutation(n)
if result == "NO SOLUTION":
    print(result)
else:
    print(" ".join(map(str, result)))
