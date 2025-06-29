check = ['M', 'O', 'B', 'I', 'S']
point = [0] * 5
for n in input():
    if n in check:
        point[check.index(n)] = 1
if sum(point) == 5:
    print('YES')
else:
    print('NO')