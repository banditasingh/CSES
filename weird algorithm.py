def weird_algorithm(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

n = int(input())

result_sequence = weird_algorithm(n)
print(" ".join(map(str, result_sequence)))
