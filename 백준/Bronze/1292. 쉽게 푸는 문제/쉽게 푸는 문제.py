A, B = map(int, input().split())   # A = 시작, B = 끝

sequence = []
for n in range(1, B + 1):
    sequence = sequence + [n] * n
sum = 0
for n in range(A-1, B):
    sum += sequence[n]

print(sum)