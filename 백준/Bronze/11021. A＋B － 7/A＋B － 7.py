T = int(input())
result = []

for _ in range(1, T+1):
    a, b = map(int, input().split())
    result.append(a + b)
    
    
for i in range(1, T+1):
    print("Case #%d: %d"%(i, result[i-1]))
