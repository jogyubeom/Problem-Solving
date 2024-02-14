icp = {'(':3, '*':2, '/':2, '+':1, '-':1}   # 스택 밖에서의 우선순위
isp = {'(':0, '*':2, '/':2, '+':1, '-':1, 0:0}   # 스택 안에서의 우선순위

for tc in range(1, 11):
    N = int(input())    # 계산식 길이
    code = input()
    post_code = ''
    top = -1
    stack = [0] * N
    for n in range(N):
        if code[n] == '(' or (code[n] in '+-*/' and icp[code[n]] > isp[stack[top]]):
            top += 1
            stack[top] = code[n]
        elif code[n] in '+-*/' and icp[code[n]] <= isp[stack[top]]:
            while icp[code[n]] <= isp[stack[top]]:
                top -= 1
                post_code += stack[top + 1]
            top += 1
            stack[top] = code[n]
        elif code[n] == ')':
            while stack[top] != '(':
                top -= 1
                post_code += stack[top + 1]
            top -= 1  # 여는 괄호 마저 하나 버려준다
            stack[top + 1]
        else:
            post_code += code[n]

        if n == N-1 and top != -1:
            while top != -1:
                top -= 1
                post_code += stack[top + 1]

    top = -1
    stack = [0] * N
    for n in post_code:
        if n not in '+*':
            top += 1
            stack[top] = int(n)
        elif n == '+':
            val = stack[top-1] + stack[top]
            top -= 1
            stack[top] = val
        elif n == '*':
            val = stack[top-1] * stack[top]
            top -= 1
            stack[top] = val
    result = stack[top]
    print(f'#{tc} {result}')