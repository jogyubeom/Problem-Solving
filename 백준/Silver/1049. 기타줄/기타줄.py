N, M = map(int, input().split())
six_string = 1e9
one_string = 1e9
for _ in range(M):
    six, one = map(int, input().split())
    six_string = min(six, six_string)
    one_string = min(one, one_string)
six_fold = N // 6
change = N % 6
one_buying = one_string * change
if six_string > one_string * 6:
    result = N * one_string
elif six_string < one_buying:
    result = six_string * (six_fold + 1)
else:
    result = six_string * six_fold + one_string * change
print(result)