def dfs(power, cnt):
    global max_power
    if cnt == 11:
        max_power = max(max_power, power)
        return
    for r in range(11):
        if picked[r] == 1:
            continue
        if position[r][cnt] == 0:
            continue
        picked[r] = 1
        dfs(power + position[r][cnt], cnt + 1)
        picked[r] = 0


T = int(input())
for _ in range(T):
    position = [list(map(int, input().split())) for _ in range(11)]
    picked = [0] * 11   # 뽑힌 선수 표시 (r 값)
    max_power = 0
    dfs(0, 0)
    print(max_power)
