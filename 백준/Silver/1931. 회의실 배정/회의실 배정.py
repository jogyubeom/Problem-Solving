N = int(input())
meetings = []
count = 0
for _ in range(N):
    a, b = map(int, input().split())
    meetings.append((a, b))
meetings.sort(key= lambda x: (x[0], x[1]))
end = 0
for i in range(N):
    if meetings[i][0] >= end:
        count += 1
        end = meetings[i][1]
    elif meetings[i][1] < end:
        end = meetings[i][1]
print(count)