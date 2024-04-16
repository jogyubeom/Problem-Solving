def binggo(num):
    count = 0

    for r in range(5):
        for c in range(5):
            if board[r][c] == num:
                board[r][c] = 0
                break

    for r in range(5):
        for c in range(5):
            if board[r][c] != 0:
                break
        else:
            count += 1

    for c in range(5):
        for r in range(5):
            if board[r][c] != 0:
                break
        else:
            count += 1

    for t in range(5):
        if board[t][t] != 0:
            break
    else:
        count += 1

    for d in range(5):
        if board[4-d][d] != 0:
            break
    else:
        count += 1

    return count


board = [list(map(int, input().split())) for _ in range(5)]
number_call = []
for _ in range(5):
    number_call += list(map(int, input().split()))

for n in range(25):
    if binggo(number_call[n]) >= 3:
        print(n+1)
        break
