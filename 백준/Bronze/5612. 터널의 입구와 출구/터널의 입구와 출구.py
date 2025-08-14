N = int(input())
cars = int(input())
res = cars
for i in range(N):
    a, b = map(int, input().split())
    cars += a - b
    res = max(res, cars)
    if cars < 0:
        res = 0
        break
print(res)
