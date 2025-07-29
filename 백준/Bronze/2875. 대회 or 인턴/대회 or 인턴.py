N, M, K = map(int, input().split())
res = min(N // 2, M)
N -= 2 * res
M -= res
tmp = N + M
tmp -= K
while tmp < 0:
    res -= 1
    tmp += 3
if res < 0:
    res = 0
print(res)
    
