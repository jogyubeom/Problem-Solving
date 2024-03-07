N = int(input())
arr = list(map(int, input().split()))
v = int(input())
count = 0
for n in range(N):
    if arr[n] == v:
        count += 1
print(count)