dr = [1, 1, 1, 0]     # 아래, 우대각, 좌대각, 우
dc = [0, 1, -1, 1]

T = int(input())  # 테스트 케이스
for tc in range(1, 1 + T):
    N = int(input())  # 오목판 크기
    adjl = [input() for _ in range(N)]  # 오목판
    result = 'NO'
    success = False
    for i in range(N):
        if success is True:
            break
        for j in range(N):
            if success is True:
                break
            if adjl[i][j] == 'o':
                for t in range(4):
                    count = 1
                    for b in range(1,5):
                        r = i + dr[t] * b
                        c = j + dc[t] * b
                        if r < 0 or c < 0 or r > N-1 or c > N-1:
                            break
                        if adjl[r][c] == 'o':
                            count += 1
                    if count == 5:
                        result = 'YES'
                        success = True
                        break

    print(f'#{tc} {result}')