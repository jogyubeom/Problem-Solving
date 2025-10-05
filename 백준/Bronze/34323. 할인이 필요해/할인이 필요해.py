N, M, S = map(int, input().split())
res = min(M * S, S * (M + 1) * (100 - N) // 100)
print(res)