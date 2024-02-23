S = input()     # 단어 입력
for abc in 'abcdefghijklmnopqrstuvwxyz':
    for n in range(len(S)):
        if abc == S[n]:
            print(n, end=' ')
            break
    else:
        print(-1, end=' ')