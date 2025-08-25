arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for _ in range(int(input())):
    temp = 2015
    word = input()
    check = [0] * 26
    for w in word:
        check[arr.index(w)] = 1
    for i in range(26):
        if check[i] == 1:
            temp -= i + 65
            
    print(temp)