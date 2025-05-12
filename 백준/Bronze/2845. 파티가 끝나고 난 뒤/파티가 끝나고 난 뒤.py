L, P = map(int, input().split())
pp = L * P
news = list(map(int, input().split()))
for n in news:
    print(n - pp, end=' ')