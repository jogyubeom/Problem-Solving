def ladder_down(r,c):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # 우 하 좌 상 0 1 2 3
    d = 1
    count = 0
    while r < 99:
        if c > 0 and ladders[r][c-1] == 1:
            d = 2
            while ladders[r][c-1] == 1:
                ladders[r + dr[d]][c + dc[d]]
                r = r + dr[d]
                c = c + dc[d]
                count += 1
                if c == 0:
                    break
        elif c < 99 and ladders[r][c+1] == 1:
            d = 0
            while ladders[r][c + 1] == 1:
                ladders[r + dr[d]][c + dc[d]]
                r = r + dr[d]
                c = c + dc[d]
                count += 1
                if c == 99:
                    break
        d = 1
        ladders[r + dr[d]][c + dc[d]]
        r = r + dr[d]
        c = c + dc[d]
        count += 1

    return count

for _ in range(10):
    T = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]
    start = []
    for c in range(100):
        if ladders[0][c] == 1:
            start.append(c)
    min_start = 10000
    for c in start:
        if ladder_down(0, c) < min_start:
            min_start = ladder_down(0, c)
            result = c

    print(f'#{T} {result}')