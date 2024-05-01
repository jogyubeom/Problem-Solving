dic = {1: 1, 2: 3}


def dp(n):
    if n in dic:
        return dic[n]
    dic[n] = dp(n-1) + dp(n-2) * 2
    return dic[n]


print(dp(int(input())) % 10007)