arr = []
for _ in range(int(input())):
    arr.append(input().split())
arr.sort(key=lambda x: int(x[0]))
for l in arr:
    print(' '.join(l))