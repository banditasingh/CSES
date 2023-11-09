n=int(input())
numbers = list(map(int, input().split()))

def missing_numbers(n,numbers):
    total_sum = n * (n + 1) // 2
    given_sum = sum(numbers)
    missing_number = total_sum - given_sum

    
    return missing_number

result = missing_numbers(n, numbers)
print(result)