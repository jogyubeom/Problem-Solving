a, b = map(int, input().split())
t = 1
for _ in range(a):
    for i in range(b):
        if i == b-1:
            print(t)
        else:
            print(t, end=" ")
        t += 1