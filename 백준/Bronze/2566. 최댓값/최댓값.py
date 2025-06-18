board = [list(map(int, input().split())) for _ in range(9)]
max_value = 0
x = 0
y = 0

for i in range(9):
    for j in range(9):
        if board[i][j] > max_value:
            max_value = board[i][j]
            x = i
            y = j
            
print(max_value)
print(x + 1, y + 1)