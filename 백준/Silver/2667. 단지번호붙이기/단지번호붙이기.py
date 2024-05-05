from collections import deque


def bfs(a, b):
    global count
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    que = deque()
    que.append([a, b])
    while que:
        r, c = que.popleft()
        for t in range(4):
            nr = r + dr[t]
            nc = c + dc[t]
            if nc < 0 or nr < 0 or nc >= N or nr >= N:
                continue
            if ground[nr][nc] == 1:
                count += 1
                ground[nr][nc] = 0
                que.append([nr, nc])


N = int(input())    # 한 변의 길이
ground = [list(map(int, input())) for _ in range(N)]
department = []
for R in range(N):
    for C in range(N):
        if ground[R][C] == 1:
            count = 1
            ground[R][C] = 0
            bfs(R, C)
            department.append(count)
L = len(department)
print(L)
department.sort()
for i in range(L):
    print(department[i])
