
def build(i, j, N):
    global white_count, blue_count
    color = paper[i][j]
    for r in range(i, i+N):
        for c in range(j, j+N):
            if paper[r][c] != color:
                N = N // 2
                build(i, j, N)
                build(i + N, j, N)
                build(i, j + N, N)
                build(i + N, j + N, N)
                return
    if color == 0:
        white_count += 1
    else:
        blue_count += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white_count = 0
blue_count = 0
build(0, 0, N)

print(white_count)
print(blue_count)