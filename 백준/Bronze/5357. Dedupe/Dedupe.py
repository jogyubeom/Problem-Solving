for _ in range(int(input())):
    text = input()
    l = len(text)
    before = text[0]
    res = before
    for i in range(1, l):
        if text[i] == before:
            continue
        else:
            res += text[i]
        before = text[i]
    print(res)