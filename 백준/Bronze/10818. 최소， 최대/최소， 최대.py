N = input()
numbers = list(map(int, input().split()))
max_v = -1000000
min_v = 1000000
for n in numbers:
    if n > max_v:
        max_v = n
    if n < min_v:
        min_v = n
print(min_v, max_v)