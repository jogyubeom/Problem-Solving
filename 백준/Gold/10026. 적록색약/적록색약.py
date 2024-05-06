from collections import deque


def bfs(r, c):
    global count1, count2
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    que = deque()
    que.append([r, c])
    while que:
        a, b = que.popleft()
        color = painting[a][b]
        for t in range(4):
            nr = a + dr[t]
            nc = b + dc[t]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if painting[nr][nc] == color and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                que.append([nr, nc])


N = int(input())
painting = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
count1 = 0
count2 = 0
for R in range(N):
    for C in range(N):
        if visited[R][C] == 0:
            visited[R][C] = 1
            count1 += 1
            bfs(R, C)

for R in range(N):
    for C in range(N):
        if painting[R][C] == 'R':
            painting[R][C] = 'G'

visited = [[0] * N for _ in range(N)]
for R in range(N):
    for C in range(N):
        if visited[R][C] == 0:
            visited[R][C] = 1
            count2 += 1
            bfs(R, C)

print(count1, count2)
