N, M = map(int, input().split())
NotSee = set()
NotHear = set()
for _ in range(N):
    NotSee.add(input())
for _ in range(M):
    NotHear.add(input())
result = NotSee & NotHear
result = list(result)
result.sort()
print(len(result))
for p in result:
    print(p)
