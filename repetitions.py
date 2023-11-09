n= input().strip()

def repetiton(n):
    max_rep =1
    current_rep =1

    for i in range(1,len(n)):
        if n[i] == n[i-1]:
            current_rep += 1
            max_rep = max(max_rep,current_rep)
        else:
            current_rep = 1
    return max_rep

result = repetiton(n)
print(result)            