def prime_divide(N, n):
    count = 0
    while N % n == 0:
        N = N // n
        count += 1
    return count

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = []
    for n in [2, 3, 5, 7, 11]:
        ans = prime_divide(N, n)
        result.append(ans)

    print(f'#{tc}', end=' ')
    print(*result)