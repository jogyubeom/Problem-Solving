
def dfs(cnt, s):
    if s == 6:
        print(*S)
        return
    elif cnt == k:
        return
    if s + k - cnt < 6:
        return
    S.append(arr[cnt])
    dfs(cnt+1, s+1)
    S.pop()
    dfs(cnt+1, s)


while True:
    arr = list(map(int, input().split()))   # k와 집합 s
    if arr[0] == 0:
        break
    k = arr.pop(0)
    S = []
    dfs(0, 0)
    print()
