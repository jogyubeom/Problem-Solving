a, b = map(int, input().split())
c, d = map(int, input().split())

res = []
res.append(a/c + b/d)
res.append(c/d + a/b)
res.append(d/b + c/a)
res.append(b/a + d/c)

print(res.index(max(res)))