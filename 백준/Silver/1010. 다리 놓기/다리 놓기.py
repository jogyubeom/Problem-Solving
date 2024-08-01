T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    num1 = 1
    for _ in range(N):
        num1 *= M
        M -= 1
    num2 = 1
    while N != 1:
        num2 *= N
        N -= 1
    print(num1//num2)