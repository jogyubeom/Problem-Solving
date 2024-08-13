word1 = input()
word2 = input()
word3 = input()
words = ['FizzBuzz', 'Fizz', 'Buzz']

def process(w):
    if w % 3 == 0 and w % 5 == 0:
        return 'FizzBuzz'
    elif w % 3 == 0:
        return 'Fizz'
    elif w % 5 == 0:
        return 'Buzz'
    else:
        return w

if word3 not in words:
    print(process(int(word3) + 1))
elif word2 not in words:
    print(process(int(word2) + 2))
elif word1 not in words:
    print(process(int(word1) + 3))
