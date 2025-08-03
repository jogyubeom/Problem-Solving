N = int(input())
for i in range(N):
    one = " " * (N - i - 1) + "*" * i
    two = "*" * i
    print(one + "*" + two)