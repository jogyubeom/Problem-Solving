T = int(input())
for tc in range(T):
    case, length = input().split()
    arr = input().split()
    order = [0] * 10
    list = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    for n in range(int(length)):
        for i in range(10):
            if arr[n] == list[i]:
                order[i] += 1
    result = []
    for n in range(10):
        result += [list[n]] * order[n]

    print(f'{case}')
    print(*result)