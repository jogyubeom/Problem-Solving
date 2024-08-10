def search(W):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    num = 1
    for n in range(len(alphabet)):
        if W == alphabet[n]:
            return num + n

L = int(input())
word = input()
result = 0
for i in range(L):
    result += search(word[i]) * 31**i
result %= 1234567891
print(result)
