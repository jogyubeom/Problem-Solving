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


for tc in range(10):
    N = int(input())
    code = input()    # 코드 입력
    size = N
    stack = [0] * size
    top = -1
    result = 1
    for n in code:
        if n == '{' or n == '(' or n == '[' or n == '<':
            push(n)
        if n == '}':
            if pop() != '{':
                result = 0
                break
        if n == ')':
            if pop() != '(':
                result = 0
                break
        if n == '>':
            if pop() != '<':
                result = 0
                break
        if n == ']':
            if pop() != '[':
                result = 0
                break
    if top != -1:
        result = 0
    print(f'#{tc+1} {result}')