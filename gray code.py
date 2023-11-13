def generate_gray_code(n):
    if n == 0:
        return ['0']
    if n == 1:
        return ['0', '1']

    prev_gray_code = generate_gray_code(n - 1)
    gray_code = []

    for code in prev_gray_code:
        gray_code.append('0' + code)

    for code in reversed(prev_gray_code):
        gray_code.append('1' + code)

    return gray_code

def print_gray_code(n):
    gray_code = generate_gray_code(n)
    for code in gray_code:
        print(code)

# Example usage:
n = int(input())
print_gray_code(n)
