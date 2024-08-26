N = int(input())
products = []
for _ in range(N):
    a, b = map(int, input().split())
    products.append((a, b))
products.sort(key= lambda x:(-x[0], x[1]))
print(*products[0], end=' ')
print(*products[1])
products.sort(key= lambda x:(x[1], -x[0]))
print(*products[0], end=' ')
print(*products[1])
