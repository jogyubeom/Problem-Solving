def push(item):
    global top
    if top == size - 1:
        return 'overflow'
    top += 1
    stack[top] = item


def pop():
    global top
    if top == -1:
        return 'empty'
    top -= 1
    return stack[top + 1]


T = int(input())
for tc in range(T):
    N = int(input())    # 줄 수
    print(f'#{tc + 1}')
    size = N
    stack = [0] * size
    stack[0] = 1
    top = -1
    for i in range(1, N + 1):
        pre_stack = stack[:]
        stack = [0] * size
        stack[0] = 1
        top = -1
        for j in range(i):
            push(pre_stack[j] + pre_stack[j-1])
        stack[0] = 1
        print(*stack[:top+1])