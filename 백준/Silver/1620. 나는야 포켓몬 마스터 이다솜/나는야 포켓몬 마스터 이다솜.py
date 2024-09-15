
N, M = map(int, input().split())
poketmons = dict()
for i in range(N):
    poketmon = input()
    poketmons[str(i+1)] = poketmon
    poketmons[poketmon] = i+1
for _ in range(M):
    print(poketmons[input()])