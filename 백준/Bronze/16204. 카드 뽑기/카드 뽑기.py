N, M, K = map(int, input().split())
res = min(M, K) + min(N - M, N - K)
print(res)