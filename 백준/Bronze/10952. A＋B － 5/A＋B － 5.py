al = []
bl = []
count = 0
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:     
        al.append(a)
        bl.append(b)
        count += 1
for i in range(count):
    print(al[i]+bl[i])
