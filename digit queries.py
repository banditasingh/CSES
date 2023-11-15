for x in[int(input()) for j in range(int(input()))]:
    digit,length=1,1
    while x>digit*length*9:
        x-=digit*length*9
        digit,length=digit*10,length+1
    number,remain=divmod(x-1,length)
    print(str(number+digit)[remain])
3

