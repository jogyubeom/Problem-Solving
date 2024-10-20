N = int(input())
time = list(map(int, input().split()))
time.sort()
result = 0
count = N
for i in range(N):
    result += time[i] * count
    count -= 1
print(result)