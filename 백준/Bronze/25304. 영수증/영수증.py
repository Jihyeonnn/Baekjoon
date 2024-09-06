hap = int(input())
n = int(input())
sum = 0
for _ in range(n):
    won, gae = map(int,input().split())
    sum = sum + (won * gae)

if hap == sum:
    print("Yes")
else: print("No")
