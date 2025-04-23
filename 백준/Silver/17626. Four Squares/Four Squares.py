
import sys
input = sys.stdin.readline

n = int(input())
num = 1
dp = [0] * (n+1)

while num**2 <= n:
    dp[num**2] = 1
    num += 1

for i in range(2, n+1):
    if dp[i] != 0:
        continue

    for j in range(1, int(i**0.5) + 1):
        if dp[i] == 0:
            dp[i] = 1 + dp[i-j**2]
        else:
            dp[i] = min(dp[i], 1 + dp[i-j**2])

print(dp[n])