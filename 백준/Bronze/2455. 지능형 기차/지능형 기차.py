res = 0
temp = 0
for _ in range(4):
    x, y = map(int, input().split())   
    temp -= x
    temp += y
    res = max(res, temp)
print(res)