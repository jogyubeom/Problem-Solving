
dr = [-1, 0, 1, 0]     # 상 우 하 좌
dc = [0, 1, 0, -1]


def dfs(r, c, path):
    if len(path) == 7:
        result.add(path)
        return
    for t in range(4):
        nr = r + dr[t]
        nc = c + dc[t]
        if nr < 0 or nc < 0 or nr >= 4 or nc >= 4:
            continue
        dfs(nr, nc, path + maps[nr][nc])


T = int(input())
for tc in range(1, 1+T):
    maps = [input().split() for _ in range(4)]   # 격자판
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])
    print(f'#{tc} {len(result)}')