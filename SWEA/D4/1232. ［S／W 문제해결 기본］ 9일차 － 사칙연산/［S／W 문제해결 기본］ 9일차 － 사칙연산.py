def inorder(v):
    if left[v]:
        inorder(left[v])
        inorder(right[v])
    if val[v] not in '+-*/':
        return
    if val[v] == '+':
        val[v] = int(val[left[v]]) + int(val[right[v]])
    elif val[v] == '-':
        val[v] = int(val[left[v]]) - int(val[right[v]])
    elif val[v] == '*':
        val[v] = int(val[left[v]]) * int(val[right[v]])
    elif val[v] == '/':
        val[v] = int(val[left[v]]) / int(val[right[v]])


for tc in range(1, 11):
    N = int(input())   # 정점의 개수
    left = [0] * (N+1)
    right = [0] * (N+1)
    val = [0] * (N+1)
    for _ in range(N):
        inf = input().split()
        inf[0] = int(inf[0])
        if inf[1] in '+-*/':
            val[inf[0]] = inf[1]
            left[inf[0]] = int(inf[2])
            right[inf[0]] = int(inf[3])
        else:
            val[inf[0]] = inf[1]
    inorder(1)
    result = int(val[1])

    print(f'#{tc} {result}')
