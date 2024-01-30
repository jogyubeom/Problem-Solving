N = int(input())
level_list = []
for _ in range(N):
    level_list.append(int(input()))
count = 0
for n in range(N-1,0,-1):
    while level_list[n] <= level_list[n-1]:
        level_list[n-1] -= 1
        count += 1

print(count)