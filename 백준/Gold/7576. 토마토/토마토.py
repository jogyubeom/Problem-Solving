from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

que = deque()

for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            que.append([r, c])

while que:
    r, c = que.popleft()

    for t in range(4):
        nr = r + dr[t]
        nc = c + dc[t]

        if nr >= 0 and nr < N and nc >= 0 and nc < M and box[nr][nc] == 0:
            box[nr][nc] = box[r][c] + 1
            que.append([nr, nc])
count = 0

for r in range(N):
    for c in range(M):
        if box[r][c] == 0:
            print(-1)
            exit(0)
        count = max(count, box[r][c])
print(count - 1)
