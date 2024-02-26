import sys


def pick(M):
    if M == 0:
        print(*result)
        return
    flag = 0
    for n in range(N):
        if index_record[n] == 0 and flag != arr[n]:
            if len(result) == 0:
                result.append(arr[n])
                index_record[n] = 1
                flag = arr[n]
                pick(M-1)
                result.pop()
                index_record[n] = 0
            elif result[-1] <= arr[n]:
                result.append(arr[n])
                index_record[n] = 1
                flag = arr[n]
                pick(M - 1)
                result.pop()
                index_record[n] = 0


N, M = map(int, sys.stdin.readline().split())    # 자연수, 고를 개수
arr = list(map(int, sys.stdin.readline().split()))   # N개의 자연수 리스트
arr.sort()
result = []
index_record = [0] * N
pick(M)