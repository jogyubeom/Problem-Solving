T = int(input())    # 테스트 케이스 개수
for tc in range(1, 1+T):
    text_arr = [input() for _ in range(5)]
    result = ''
    n = 0
    while n < 15:
        plus_text = ''
        for text in text_arr:
            if n < len(text):
                plus_text += text[n]
        result += plus_text
        n += 1

    print(f'#{tc} {result}')