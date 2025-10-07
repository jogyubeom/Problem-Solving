N, W, H, L = map(int, input().split())
res = (W // L) * (H // L)
print(min(N, res))