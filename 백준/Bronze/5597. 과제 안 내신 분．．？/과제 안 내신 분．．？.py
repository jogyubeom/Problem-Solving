attendance_list = []
for n in range(1,31):
    attendance_list.append(n)

for n in range(28):
    submit_num = int(input())
    attendance_list.remove(submit_num)

print(min(attendance_list))
print(max(attendance_list))