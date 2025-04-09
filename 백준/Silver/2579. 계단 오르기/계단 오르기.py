import sys
input = sys.stdin.readline
    
N = int(input())    # 계단 개수
stairs = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N + 1)
if N <= 1:
    print(stairs[N])
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    if N > 2:
        for i in range(3, N + 1):
            dp[i] = max(stairs[i - 1] + dp[i - 3], dp[i - 2]) + stairs[i]

    print(dp[N])
