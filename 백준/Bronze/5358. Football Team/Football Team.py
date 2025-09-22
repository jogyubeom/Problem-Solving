while True:
    try:
        word = input()
        res = ''
        for w in word:
            if w == 'e':
                res += 'i'
            elif w == 'i':
                res += 'e'
            elif w == 'E':
                res += 'I'
            elif w == 'I':
                res += 'E'
            else:
                res += w
        print(res)
    except:
        break