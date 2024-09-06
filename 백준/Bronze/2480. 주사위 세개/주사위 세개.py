a,b,c = map(int,input().split())
result =  0
same = 0
if a==b==c:
    same = a
    result = 10000+same*1000
elif a==b or b==c or a==c:
    if a==b: 
        same = a
    elif b==c:
        same = b
    elif a==c:
        same = c
    result = 1000+same*100
elif a!=b!=c:
    same = max(a,b,c)
    result = 100 * same

print(result)