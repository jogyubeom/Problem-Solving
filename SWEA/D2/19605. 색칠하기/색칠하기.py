T = int(input())
for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]
    N = int(input())
    for n in range(N):
        r1, c1, r2, c2, color = map(int,input().split())
        if color == 1:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if arr[r][c] == 0 or arr[r][c] == 2:
                        arr[r][c] += 1
        else:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if arr[r][c] == 0 or arr[r][c] == 1:
                        arr[r][c] += 2
    count = 0
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:
                count += 1
    print(f'#{tc} {count}')