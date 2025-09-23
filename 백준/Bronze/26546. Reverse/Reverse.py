for _ in range(int(input())):
    word, a, b = input().split()
    a = int(a)
    b = int(b)
    one = ''
    two = ''
    if a > 0:
        one = word[:a]
    if b < len(word):
        two = word[b:]
    print(one + two)