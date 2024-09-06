al = []
bl = []
count = 0
while True:
    try:
        a, b = map(int, input().split())
        al.append(a)
        bl.append(b)
        count += 1
    except:
        break
for i in range(count):
    print(al[i]+bl[i])
