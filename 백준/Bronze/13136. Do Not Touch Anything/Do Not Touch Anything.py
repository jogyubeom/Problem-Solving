R, C, N = map(int, input().split())
r = R // N + 1 if R % N else R // N
c = (C // N + 1) if (C % N) else (C // N)
print(r * c)