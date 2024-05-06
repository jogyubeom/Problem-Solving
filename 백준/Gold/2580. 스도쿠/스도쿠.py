def row_check(R ,num):
    for c in range(9):
        if board[R][c] == num:
            return False
    return True


def col_check(C, num):
    for r in range(9):
        if board[r][C] == num:
            return False
    return True


def rec_check(R, C, num):
    for r in range(3):
        for c in range(3):
            if board[R // 3 * 3 + r][C // 3 * 3 + c] == num:
                return False
    return True


def dfs(n):
    if n == blank_num:
        for line in board:
            print(*line)
        exit(0)
    a, b = blank[n]
    for i in range(1, 10):
        if row_check(a, i) and col_check(b, i) and rec_check(a, b, i):
            board[a][b] = i
            dfs(n+1)
            board[a][b] = 0


board = [list(map(int, input().split())) for _ in range(9)]
blank = []
for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            blank.append([r, c])
blank_num = len(blank)
dfs(0)
