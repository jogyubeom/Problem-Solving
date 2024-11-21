import sys

input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
sum_lst = sum(arr)
result = 0
for i in range(N-1):
    sum_lst -= arr[i]
    result += arr[i] * sum_lst
print(result % 1000000007)