count=int(input())
save_list = []
for i in range(count):
    save=list(map(str,input()))
    save_list.append(save[0]+save[-1])
for i in range(count):
    print(save_list[i])
