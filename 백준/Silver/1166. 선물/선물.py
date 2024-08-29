N, L, W, H = map(int, input().split())
s = 0
e = min(L, W, H)
for i in range(100):
    m = (s + e) / 2
    if (L//m) * (W//m) * (H//m) >= N:
        s = m
    else:
        e = m
print(e)