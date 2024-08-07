
def factorial(num):
    if num == 0 or num == 1:
        return 1
    res = 1
    for n in range(2, num+1):
        res *= n
    return res

N, K = map(int, input().split())
result = factorial(N) / ( factorial(N-K) * factorial(K) )
print(int(result))
