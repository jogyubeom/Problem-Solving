num_list = []
for n in range(9):
    num_list.append(int(input()))

max_num = max(num_list)

for n in range(9):
    if num_list[n] == max_num:
        max_index = n + 1

print(max_num)
print(max_index)
