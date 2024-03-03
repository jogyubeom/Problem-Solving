N = int(input())
count = 0
num_list = list(map(int, input().split()))
for num in num_list:
    if num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        count += 1
print(count)