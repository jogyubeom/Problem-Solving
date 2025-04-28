a, b, c = map(int, input().split())
h = int(input())

c += h
b += c // 60
c = c % 60

a += b // 60
b = b % 60

a = a % 24

print(a, b, c)
