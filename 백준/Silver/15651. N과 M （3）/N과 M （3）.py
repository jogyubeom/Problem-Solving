def pick(M):
    if M == 0:
        print(*result)
        return
    for n in arr:
        result.append(n)
        pick(M-1)
        result.pop()
    return


N, M = map(int, input().split())    # 수열 크기, 고를 개수
arr = list(range(1, N+1))
result = []
pick(M)