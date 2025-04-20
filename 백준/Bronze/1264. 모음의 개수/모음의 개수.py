
vowel = ['a','A','e','E','i','I','o','O','u','U']
while True:
    words = input()
    if words == '#':
        break
    count = 0
    for n in words:
        if n in vowel:
            count += 1
    print(count)