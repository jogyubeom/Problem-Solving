res = 0
t = int(input())
res += 8 * (t-1)
temp = list(map(int, input().split()))
for i in temp:
    res += i

print(res // 24, res % 24)