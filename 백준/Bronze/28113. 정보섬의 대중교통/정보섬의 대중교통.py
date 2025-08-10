N, A, B = map(int, input().split())
temp = max(N, B)
if temp == A:
    print('Anything')
elif temp < A:
    print('Subway')
else:
    print('Bus')