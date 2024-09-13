
N = int(input())

def check(r, c, t):
    rt = [1, 0, -1, 0]  # 하 좌 상 우
    ct = [0, -1, 0, 1]
    count = 0
    while True:
        r += rt[t]
        c += ct[t]
        if r < 0 or r >= N or c < 0 or c >= N or board[r][c] != '*':
            break
        count += 1
    return count


board = [input() for _ in range(N)]
# 심장 찾기
flag = False
for r in range(N):
    if flag is True:
        break
    for c in range(N):
        if board[r][c] == '*':
            heart = (r+1, c)
            flag = True
            break
print(heart[0] + 1, heart[1] + 1)
result = []

# 왼쪽 팔 길이
result.append(check(heart[0], heart[1], 1))
# 오른쪽 팔 길이
result.append(check(heart[0], heart[1], 3))
# 허리 길이
wrist_length = check(heart[0], heart[1], 0)
result.append(wrist_length)
# 왼쪽 다리 길이
result.append(check(heart[0] + wrist_length, heart[1]-1, 0))
# 오른쪽 다리 길이
result.append(check(heart[0] + wrist_length, heart[1]+1, 0))

print(*result)