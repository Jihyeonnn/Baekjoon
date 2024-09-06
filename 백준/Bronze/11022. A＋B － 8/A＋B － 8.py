T = int(input())
c = []
al = []
bl = []

for _ in range(1, T+1):
    a, b = map(int, input().split())
    al.append(a)
    bl.append(b)
    c.append(a + b)
    
    
for i in range(1, T+1):
    print("Case #%d: %d + %d = %d"%(i, al[i-1], bl[i-1], c[i-1]))
