n_list = list(int(input()) for _ in range(9))
max_index = n_list.index(max(n_list)) + 1

print(max(n_list))
print(max_index)
