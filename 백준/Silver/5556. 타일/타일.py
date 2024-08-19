N = int(input())
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    if a > (N + 1) / 2:
        a = N - a + 1
    if b > (N + 1) / 2:
        b = N - b + 1
    if a > b:
        result = b % 3
    else:
        result = a % 3
    if result == 0:
        print(3)
    else:
        print(result)
