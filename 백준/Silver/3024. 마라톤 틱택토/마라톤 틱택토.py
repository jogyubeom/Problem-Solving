
N = int(input())
board = []
for _ in range(N):
    board.append(input())
flag = False


def check(W, r, c):
    # 우 하 우하 좌하
    tr = [0, 1, 1, 1]
    tc = [1, 0, 1, -1]
    for t in range(4):
        count = 1
        for z in range(1, 3):
            nr = r + tr[t] * z
            nc = c + tc[t] * z
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == W:
                    count += 1
                else:
                    break
                if count == 3:
                    return True
    return False
        

for r in range(N):
    if flag is True:
        break
    for c in range(N):
        word = board[r][c]
        if word == '.':
            continue
        elif check(word, r, c) is True:
            flag = True
            print(word)
            break
else:
    print('ongoing')
