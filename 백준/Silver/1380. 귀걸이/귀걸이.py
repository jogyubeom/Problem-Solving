count = 1
while True:
    n = int(input())
    if n == 0:
        break
    girls = []
    for _ in range(n):
        girls.append(input())
    check = [2] + ([0] * n)
    for _ in range(2 * n - 1):
        num, ab = input().split()
        check[int(num)] += 1
    for i in range(n+1):
        if check[i] != 2:
            print(count, girls[i-1])
    count += 1
