T = int(input())
for tc in range(1, 1 + T):
    N = int(input())    # 학생 수
    move = []
    for _ in range(N):
        a = list(map(int, input().split()))
        a.sort()
        s, e = a[0], a[1]
        if s % 2 == 0:
            s -= 1
        if e % 2 == 0:
            e -= 1
        move.append((s, e))
    move.sort
    visited = [0] * 400     # 복도
    max_v = 1
    for n in range(N):
        for i in range(move[n][0], move[n][1] + 1):
            visited[i] += 1
            max_v = max(visited[i], max_v)
    print(f'#{tc} {max_v}')