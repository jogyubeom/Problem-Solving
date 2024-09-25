def next(W):
    result = []
    for n in W:
        if len(result) != 0 and result[-1] == n:
            result[-2] = str(int(result[-2]) + 1)
            continue
        result.append('1')
        result.append(n)
    # print(f'next: {result}')
    return ''.join(result)


def check(W):
    if len(W) % 2 == 1:
        return W
    result = ''
    for i in range(0, len(W), 2):
         result += int(W[i]) * W[i + 1]
    # print(f'result: {result}')
    if next(result) != W:
        return W
    if result == W:
        return W
    else:
        return check(result)


count = 1
while True:
    word = input()
    if word == '0':
        break
    print(f'Test {count}: {check(word)}')
    count += 1