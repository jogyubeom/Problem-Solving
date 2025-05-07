import sys
input = sys.stdin.readline


dy = [-1, 0, 1, 0]  # 상 우 하 좌
dx = [0, 1, 0, -1]
    
N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

min_h = 1e9
max_h = 0

for i in range(N):
    for j in range(M):
        min_h = min(min_h, ground[i][j])
        max_h = max(max_h, ground[i][j])
        
heights = list(range(min_h, max_h + 1))
heights.sort(reverse=True)

time = 1e9
result = 0

for h in heights:
    block = B
    second = 0
    flag = False
    for i in range(N):
        if flag == True:
            break
        for j in range(M):
            now = ground[i][j]
            if now == h:
                continue
            elif now > h:
                second += 2 * (now - h)
                block += (now - h)
                if second >= time:
                    flag = True
                    break
            else:
                block -= (h - now)

                second += (h - now)
                if second >= time:
                    flag = True
                    break
    
    if block < 0:
        flag = True
        continue

    if flag == False:
        time = second
        result = h

print(time, result)