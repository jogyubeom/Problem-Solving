T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    n = 0
    result = 'ON'
    for _ in range(N):
        if M & (1 << n):
            pass
        else:
            result = 'OFF'
        n += 1
    print(f'#{tc} {result}')