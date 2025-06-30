see = ['N', 'E', 'S', 'W']
now = 0
for _ in range(10):
    temp = int(input())
    if temp == 1:
        now += 1
    elif temp == 2:
        now += 2
    else:
        now -= 1
now %= 4
print(see[now])