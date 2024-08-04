words = set()
for _ in range(int(input())):
    words.add(input())

words = list(words)
words.sort()
word_count = len(words)
length = 0

while word_count != 0:
    length += 1
    for i in range(len(words)):
        if len(words[i]) == length:
            print(words[i])
            word_count -= 1
