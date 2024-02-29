import sys


number = int(input())    # 사진틀 개수
N = int(input())   # 추천 횟수
arr = list(map(int, sys.stdin.readline().split()))   # 추천들
frame = dict()  # 사진틀
visited = []    # 추천받은 학생 순서 기록
for i in range(N):
    if arr[i] not in frame and len(frame) == number:
        min_cert = min(frame, key=frame.get)    # 추천 가장 적게 받은 학생
        count = 0
        min_v = frame[min_cert]
        for n in frame.values():
            if n == min_v:
                count += 1
        if count >= 2:
            for s in visited:
                if s in [k for k, v in frame.items() if v == min_v]:
                    del frame[s]
                    visited.remove(s)
                    break
        else:
            del frame[min_cert]
    if arr[i] in frame:
        frame[arr[i]] += 1
        if arr[i] not in visited:
            visited.append(arr[i])
    else:
        frame[arr[i]] = 1
        if arr[i] not in visited:
            visited.append(arr[i])
lst = list(frame.keys())
lst.sort()
print(*lst)