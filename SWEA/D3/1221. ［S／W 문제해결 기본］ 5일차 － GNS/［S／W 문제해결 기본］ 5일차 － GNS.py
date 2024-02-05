T = int(input())
for tc in range(T):
    case, length = input().split()
    arr = input().split()
    order = [0] * 10
    for n in arr:
        if n == 'ZRO':
            order[0] += 1
        elif n == 'ONE':
            order[1] += 1
        elif n == 'TWO':
            order[2] += 1
        elif n == 'THR':
            order[3] += 1
        elif n == 'FOR':
            order[4] += 1
        elif n == 'FIV':
            order[5] += 1
        elif n == 'SIX':
            order[6] += 1
        elif n == 'SVN':
            order[7] += 1
        elif n == 'EGT':
            order[8] += 1
        elif n == 'NIN':
            order[9] += 1
    result = ['ZRO'] * order[0] +\
    ['ONE'] * order[1] +\
    ['TWO'] * order[2] +\
    ['THR'] * order[3] +\
    ['FOR'] * order[4] +\
    ['FIV'] * order[5] +\
    ['SIX'] * order[6] +\
    ['SVN'] * order[7] +\
    ['EGT'] * order[8] +\
    ['NIN'] * order[9]

    print(f'{case}')
    print(*result)