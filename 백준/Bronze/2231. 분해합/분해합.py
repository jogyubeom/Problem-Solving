N = int(input())
for n in range(1, N):
    num = sum(list(map(int, str(n))))
    result = num + n
    if result == N:
        print(n)
        break
else:
    print(0)