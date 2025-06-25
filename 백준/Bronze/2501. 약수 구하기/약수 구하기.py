
N, K = map(int, input().split())
arr = []
temp = 1
while temp <= N**0.5:
    if N % temp == 0:
        arr.append(temp)
        if temp != N // temp:
            arr.append(N // temp)
    temp += 1
arr.sort()
if len(arr) < K:
    print(0)
else:
    print(arr[K-1])