N = int(input())
count = N
space = " "
star = "*"
for i in range(1, N+1):
    count = count - 1
    print((space * count)+(star*i))
