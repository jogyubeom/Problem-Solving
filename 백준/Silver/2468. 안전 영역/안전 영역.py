
from collections import deque


def bfs(a, b):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    que = deque()
    que.append([a, b])
    while que:
        R, C = que.popleft()
        for t in range(4):
            nr = R + dr[t]
            nc = C + dc[t]
            if 0 <= nr < N and 0 <= nc < N and ground[nr][nc] > h and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                que.append([nr, nc])


N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]
min_rain = 1e9
max_rain = 0
for r in range(N):
    for c in range(N):
        min_rain = min(min_rain, ground[r][c])
        max_rain = max(max_rain, ground[r][c])

max_count = 0
for h in range(min_rain, max_rain):
    visited = [[0] * N for _ in range(N)]
    count = 0
    for r in range(N):
        for c in range(N):
            if ground[r][c] > h and visited[r][c] == 0:
                visited[r][c] = 1
                count += 1
                bfs(r, c)
    max_count = max(max_count, count)
if max_count == 0:
    max_count = 1
print(max_count)
