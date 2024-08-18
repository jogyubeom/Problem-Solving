M, N = map(int, input().split())
for n in range(M, N + 1):
    if n == 1:
        continue
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        print(n)