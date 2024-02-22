code_dict = {'0001101':'0','0011001':'1','0010011':'2','0111101':'3','0100011':'4',\
             '0110001':'5','0101111':'6','0111011':'7','0110111':'8','0001011':'9'}

T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())   # 배열의 세로, 가로 크기
    arr = [input() for _ in range(N)]
    for i in range(N):
        if '1' in arr[i]:
            my_code = arr[i]
            break
    for i in range(M):
        if my_code[i:i+7] in code_dict:
            for _ in range(8):
                if my_code[i:i + 7] not in code_dict:
                    break
                i += 7
            else:
                start = i - 56
                break
    code_num = ''
    for _ in range(8):
        code_num += code_dict[my_code[start:start + 7]]
        start += 7
    even_num = []
    odd_num = []
    for i in range(8):
        if (i + 1) % 2 != 0:
            odd_num.append(int(code_num[i]))
        else:
            even_num.append(int(code_num[i]))
    if (sum(odd_num) * 3 + sum(even_num)) % 10 == 0:
        result = sum(odd_num) + sum(even_num)
    else:
        result = 0

    print(f'#{tc} {result}')