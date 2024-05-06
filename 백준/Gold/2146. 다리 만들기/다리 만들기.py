from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(r, c):
    que = deque()
    que.append([r, c])
    while que:
        x, y = que.popleft()
        for t in range(4):
            nr = x + dr[t]
            nc = y + dc[t]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and graph[nr][nc]:
                visited[nr][nc] = 1
                graph[nr][nc] = num
                que.append([nr, nc])


def bfs2(i):
    que = deque()
    dist = [[-1] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if graph[r][c] == i:
                dist[r][c] = 0
                que.append([r, c])

    while que:
        x, y = que.popleft()
        for t in range(4):
            nr = x + dr[t]
            nc = y + dc[t]
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] and graph[nr][nc] != i:
                    return dist[x][y]
                elif (not graph[nr][nc]) and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[x][y] + 1
                    que.append([nr, nc])
    return 1e9


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
num = 1
length = 1e9

for r in range(N):
    for c in range(N):
        if graph[r][c] and not visited[r][c]:
            visited[r][c] = 1
            graph[r][c] = num
            bfs(r, c)
            num += 1

for i in range(1, num):
    length = min(length, bfs2(i))
print(length)
