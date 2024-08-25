board = [input() for _ in range(8)]
count = 0
for r in range(8):
    for c in range(8):
        if r % 2 == 0 and c % 2 == 0 and board[r][c] == 'F':
            count += 1
        elif r % 2 == 1 and c % 2 == 1 and board[r][c] == 'F':
            count += 1
print(count)
