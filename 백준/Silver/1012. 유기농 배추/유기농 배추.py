from collections import deque


def bfs(a, b):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    que = deque()
    que.append([a, b])
    while que:
        r, c = que.popleft()
        for t in range(4):
            nr = r + dr[t]
            nc = c + dc[t]
            if nc < 0 or nr < 0 or nc >= M or nr >= N:
                continue
            if ground[nr][nc] == 1:
                ground[nr][nc] = 0
                que.append([nr, nc])


for tc in range(1, int(input()) + 1):
    M, N, K = map(int, input().split())    # 가로(M=X), 세로(N=Y) 길이, 배추 개수
    ground = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1    # 배추 심기
    count = 0
    for R in range(N):
        for C in range(M):
            if ground[R][C] == 1:
                count += 1
                ground[R][C] = 0
                bfs(R, C)
    print(count)
