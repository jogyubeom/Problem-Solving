N = int(input())
if N == 0:
    print(1)
else:
    result = 1
    for i in range(N):
        result *= N-i
    print(result)