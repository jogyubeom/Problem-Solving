K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))
start = 1
end = max(lines)
while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in lines:
        count += i // mid
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)

