while True:
    name, age, w = input().split()
    if name == '#':
        break
        
    if int(age) > 17 or int(w) >= 80:
        print(name, 'Senior')
    
    else:
        print(name, 'Junior')
