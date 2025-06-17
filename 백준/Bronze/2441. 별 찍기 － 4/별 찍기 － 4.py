N = int(input())
for i in range(N):
    result = (' ' * i) + ('*' * (N - i))
    print(result)