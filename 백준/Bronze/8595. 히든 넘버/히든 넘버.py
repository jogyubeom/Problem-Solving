
N = int(input())
word = input()
numbers = []
num = ''
for i in range(N):
    if word[i] in '0123456789':
        num += word[i]
    else:
        if num:
            numbers.append(int(num))
            num = ''
if num:
    numbers.append(int(num))
if numbers:
    print(sum(numbers))
else:
    print(0)