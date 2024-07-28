
N = int(input())
num = 1
current = 1
order = 1

while N > current:
    current += order * 6
    order += 1
    num += 1

print(num)