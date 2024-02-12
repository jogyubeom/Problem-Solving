N = list(map(int, input().split()))
sum_n = 0
for n in N:
    sum_n += n**2
result = sum_n % 10
print(result)