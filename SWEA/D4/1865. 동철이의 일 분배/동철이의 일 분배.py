def dfs(level, percentage):
    global max_able
    if percentage <= max_able:
        return
    if level == N:
        max_able = percentage
        return
    for c in range(N):
        if visited[c] != 0:
            continue
        visited[c] = 1
        dfs(level+1, percentage*adjl[level][c]/100)
        visited[c] = 0


T = int(input())
for tc in range(1, 1+T):
    N = int(input())    # 해야할 일의 수 = 직원의 수
    adjl = [list(map(int, input().split())) for _ in range(N)]   # 업무별 성공 확률
    # (행, r = 직원, 열, c = 업무)
    max_able = 0
    visited = [0] * N   # 업무 처리 여부
    dfs(0, 1)
    max_able *= 100
    print(f'#{tc} {max_able:.6f}')