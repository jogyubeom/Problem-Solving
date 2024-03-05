arr = list(map(int, input().split()))
if arr[0] > arr[1]:
    arr[0], arr[1] = arr[1], arr[0]
a = arr[0]
b = arr[1]
for n in range(a, -1, -1):
    if a % n == 0 and b % n == 0:
        print(n)
        break
n = 1
while True:
    if (b * n) % a == 0:
        print(b*n)
        break
    n += 1