N = int(input())
n_list = list(map(int, input().split()))
find = int(input())
count = 0
for i in range(N):
    if find == n_list[i]:
        count += 1
print(count)
        
