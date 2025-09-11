pw = {
    "CU" : "see you",
    ":-)" : "I’m happy",
    ":-(" : "I’m unhappy",
    ";-)" : "wink",
    ":-P" : "stick out my tongue",
    "(~.~)" : "sleepy",
    "TA" : "totally awesome",
    "CCC" : "Canadian Computing Competition",
    "CUZ" : "because",
    "TY" : "thank-you",
    "YW" : "you’re welcome",
    "TTYL" : "talk to you later",
}

while True:
    word = input()
    if word == "TTYL":
        print(pw[word])
        break
    if word in pw:
        print(pw[word])
    else:
        print(word)