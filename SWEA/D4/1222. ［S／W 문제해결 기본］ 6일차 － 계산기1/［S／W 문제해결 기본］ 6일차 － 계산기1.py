for tc in range(1, 11):
    N = int(input())    # 계산식 길이
    code = input()
    post_code = ''
    top = -1
    stack = [0] * N
    for n in range(N):
        if code[n] == '+':
            if stack[top] == '+':
                while stack[top] == '+':
                    top -= 1
                    post_code += stack[top + 1]
            top += 1
            stack[top] = code[n]
        else:
            post_code += code[n]
        if n == N-1 and top != -1:
            while top != -1:
                top -= 1
                post_code += stack[top + 1]

    top = -1
    stack = [0] * N
    for n in post_code:
        if n != '+':
            top += 1
            stack[top] = int(n)
        elif n == '+':
            val = stack[top-1] + stack[top]
            top -= 1
            stack[top] = val
    result = stack[top]
    print(f'#{tc} {result}')