N = int(input())  # 점의 개수
dot_list = []
for _ in range(N):
    (a, b) = (map(int, input().split()))
    dot_list.append((a, b))
dot_list.sort(key= lambda x: (x[0],x[1]))
for i in range(N):
    print(*dot_list[i])