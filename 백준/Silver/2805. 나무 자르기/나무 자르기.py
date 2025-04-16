import sys
input = sys.stdin.readline
    
N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for h in trees:
        cut = h - mid
        if cut > 0:
            count += cut
    
    if count < M:
        end = mid - 1

    else:
        start = mid + 1

print(end)
    
