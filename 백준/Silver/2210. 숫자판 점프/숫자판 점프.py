dr = [-1, 0, 1, 0]     # 상우하좌
dc = [0, 1, 0, -1]


def dfs(i, j, num):
    if len(num) == 6:
        numbers.add(num)
        return
    for t in range(4):
        nr = i + dr[t]
        nc = j + dc[t]
        if nr < 0 or nc < 0 or nr > 4 or nc > 4:
            continue
        dfs(nr, nc, num + board[nr][nc])


board = [list(map(str, input().split())) for _ in range(5)]     # 숫자판
numbers = set()
for r in range(5):
    for c in range(5):
        dfs(r, c, board[r][c])
print(len(numbers))
