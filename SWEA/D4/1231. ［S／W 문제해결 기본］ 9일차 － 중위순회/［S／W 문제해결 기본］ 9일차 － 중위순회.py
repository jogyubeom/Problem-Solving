def inorder(v):
    if v > N:
        return
    inorder(v * 2)
    result.append(word[v])
    inorder(v * 2 + 1)


for tc in range(1, 11):
    N = int(input())   # 정점 개수
    word = [0] * (N + 1)
    for i in range(N):
        arr = input().split()
        nod = int(arr[0])
        word[nod] = arr[1]
    result = []
    inorder(1)

    print(f'#{tc}', end=' ')
    print(''.join(result))