n, m, k = map(int, input().split())
temp = 0
for i in range(n):
    for j in range(m):
        if temp == k:
            print(i, j)
            exit()
        temp += 1