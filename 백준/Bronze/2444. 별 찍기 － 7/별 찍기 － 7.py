N = int(input())
for i in range(N):
    one = " " * (N - i - 1) + "*" * i
    two = "*" * i
    print(one + "*" + two)
for i in range(N-2, -1, -1):
    one = " " * (N - i - 1) + "*" * i
    two = "*" * i
    print(one + "*" + two)