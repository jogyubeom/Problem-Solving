import sys


def pick(m):
    if m == 0:
        print(*result)
        return
    for n in range(new_N):
        if len(result) == 0:
            result.append(arr[n])
            pick(m - 1)
            result.pop()
        elif arr[n] >= result[-1]:
            result.append(arr[n])
            pick(m-1)
            result.pop()


N, M = map(int, sys.stdin.readline().split())    # 자연수, 고를 개수
arr = list(map(int, sys.stdin.readline().split()))   # N개의 자연수 리스트
arr = set(arr)
arr = list(arr)
new_N = len(arr)
arr.sort()
result = []
pick(M)