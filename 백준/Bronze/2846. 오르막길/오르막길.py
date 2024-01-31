N = int(input())
road = list(map(int, input().split()))
uphill = set()
result = []
for n in range(N-1):
    if road[n] < road[n+1]:
        uphill.update([n, n+1])
        if n == N - 2 and uphill != []:
            result.append(road[max(uphill)] - road[min(uphill)])
    else:
        if uphill:
            result.append(road[max(uphill)] - road[min(uphill)])
            uphill.clear()
        else:
            pass
if not result:
    result = [0]
print(max(result))