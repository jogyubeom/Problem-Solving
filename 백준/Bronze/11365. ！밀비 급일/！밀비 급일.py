while True:
    temp = input()
    if temp == 'END':
        break
    N = len(temp)
    for i in range(N-1, -1, -1):
        print(temp[i], end='')
    print()