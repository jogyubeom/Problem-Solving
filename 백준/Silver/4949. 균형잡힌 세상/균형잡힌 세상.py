
while True:
    arr = input()
    stack = []
    i = 0
    if arr == '.':
        break
    while True:
        if arr[i] == '.':
            print('yes' if len(stack) == 0 else 'no')
            break
        elif arr[i] == '(' or arr[i] == '[':
            stack.append(arr[i])
        elif arr[i] == ')':
            if len(stack) == 0:
                print('no')
                break
            pick = stack.pop()
            if pick != '(':
                print('no')
                break
        elif arr[i] == ']':
            if len(stack) == 0:
                print('no')
                break
            pick = stack.pop()
            if pick != '[':
                print('no')
                break
            
        i += 1
