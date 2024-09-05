N = int(input())
beads = list(map(int, input().split()))
beads.sort()
beads[N-1], beads[N-2] = beads[N-2], beads[N-1]
result = 0
for i in range(N):
    result += abs(beads[i] - beads[i-1])
print(result)