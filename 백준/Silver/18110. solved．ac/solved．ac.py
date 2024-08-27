def check(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())
opinions = []
for _ in range(n):
    opinions.append(int(input()))
opinions.sort()
reject = check(n * 0.15)
sum_of_opinions = 0
for i in range(reject, len(opinions) - reject):
    sum_of_opinions += opinions[i]
if opinions:
    print(check(sum_of_opinions / (n - (2 * reject))))
else:
    print(0)