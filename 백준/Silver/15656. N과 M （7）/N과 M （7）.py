def pick(M):
    if M == 0:
        print(*result)
        return

    for n in range(N):
        result.append(arr[n])
        pick(M-1)
        result.pop()


N, M = map(int, input().split())    # 자연수, 고를 개수
arr = list(map(int, input().split()))   # N개의 자연수 리스트
arr.sort()
result = []
pick(M)