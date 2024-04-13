
dr = [1, 1, -1, 0]     # 아래, 우하대각, 우상대각, 우
dc = [0, 1, 1, 1]


adjl = [list(map(int, input().split())) for _ in range(19)]  # 오목판
result = 0
success = False
for i in range(19):
    if success is True:
        break
    for j in range(19):
        if success is True:
            break
        for BW in [1, 2]:
            if adjl[i][j] == BW:
                for t in range(4):
                    if success is True:
                        break
                    count = 1
                    for b in range(1, 5):
                        r = i + dr[t] * b
                        c = j + dc[t] * b
                        if r < 0 or c < 0 or r > 18 or c > 18:
                            break
                        if adjl[r][c] == BW:
                            count += 1
                        else:
                            break
                    if count == 5:
                        flag = True
                        for bb in [-1, 5]:
                            r = i + dr[t] * bb
                            c = j + dc[t] * bb
                            if r < 0 or c < 0 or r > 18 or c > 18:
                                continue
                            elif adjl[r][c] == BW:
                                flag = False
                        if flag is True:
                            result = BW
                            ans = i+1, j+1
                            success = True
                            break

print(result)
if result != 0:
    print(*ans)
