res = 0
min_value = 1e9
for _ in range(7):
    temp = int(input())
    if temp % 2:
        res += temp
        min_value = min(min_value, temp)

if res:
    print(res)
    print(min_value)
else:
    print(-1)