n, x = map(int,input().split())
a = list(map(int, input().split()))
b = []
count = 0
for i in range(n):
    if a[i] < x:
        b.append(a[i])
        count += 1
for i in range(count):
    print(b[i], end = " ")
