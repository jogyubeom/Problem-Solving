def money(dices):
    check = [0] * 7
    for i in dices:
        check[i] += 1
    if max(check) == 3:
        return 10000 + 1000 * check.index(3)
    elif max(check) == 2:
        return 1000 + 100 * check.index(2)
    else:
        return max(dices) * 100

res = 0
for _ in range(int(input())):
    lst = list(map(int, input().split()))
    res = max(res, money(lst))
    
print(res)