from collections import deque

dr = [-1, 0, 1, 0, 0, 0]
dc = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

que = deque()

for h in range(H):
    for r in range(N):
        for c in range(M):
            if box[h][r][c] == 1:
                que.append([h, r, c])

while que:
    h, r, c = que.popleft()

    for t in range(6):
        nr = r + dr[t]
        nc = c + dc[t]
        nh = h + dh[t]
        if 0 <= nr < N and 0 <= nc < M and 0 <= nh < H and box[nh][nr][nc] == 0:
            box[nh][nr][nc] = box[h][r][c] + 1
            que.append([nh, nr, nc])
count = 0

for h in range(H):
    for r in range(N):
        for c in range(M):
            if box[h][r][c] == 0:
                print(-1)
                exit(0)
            count = max(count, box[h][r][c])
print(count - 1)
