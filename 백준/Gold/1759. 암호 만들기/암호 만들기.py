def dfs(i, arr):
    if i == C:
        vowel_num = len(arr + vowel) - len(set(arr + vowel))    # 모음 개수
        consonant_num = len(arr) - vowel_num    # 자음 개수
        if len(arr) == L and vowel_num >= 1 and consonant_num >= 2:
            print(''.join(arr))
        return
    if len(arr) > L:
        return
    arr.append(code[i])
    dfs(i+1, arr)
    arr.pop()
    dfs(i+1, arr)


L, C = map(int, input().split())    # 암호 길이, 문자 종류
code = input().split()  # 암호 문자 종류들
code.sort()
vowel = ['a', 'e', 'i', 'o', 'u']
result = []
dfs(0, result)
