from collections import deque


def check():
    dr = [-1, 0, 1, 0]  # 상우하좌
    dc = [0, 1, 0, -1]
    visited = [[0] * 5 for _ in range(5)]
    for r, c in com:
        visited[r][c] = 1
    que = deque()
    r, c = com[0]
    visited[r][c] = 0
    count = 1
    que.append([r, c])
    while que:
        r, c = que.popleft()
        for t in range(4):
            nr = r + dr[t]
            nc = c + dc[t]
            if nr < 0 or nc < 0 or nr > 4 or nc > 4:
                continue
            if visited[nr][nc] == 1:
                count += 1
                visited[nr][nc] = 0
                que.append([nr, nc])
    if count == 7:
        return True
    else:
        return False


def dfs(idx, Y, cnt):
    global result
    if Y >= 4:
        return
    if cnt > 7:
        return
    if 7-cnt > 25-idx:
        return
    if cnt == 7:
        if check():
            result += 1
        return
    for i in range(idx, 25):
        r = i // 5
        c = i % 5
        com.append([r, c])
        if board[r][c] == 'Y':
            dfs(i + 1, Y + 1, cnt+1)
        else:
            dfs(i + 1, Y, cnt + 1)
        com.pop()


board = [input() for _ in range(5)]     # 자리 배치
result = 0  # 7공주 경우의 수
com = []
dfs(0, 0, 0)
print(result)
