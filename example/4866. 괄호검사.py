T = int(input())
for t in range(T):
    string = [i for i in input()]
    check = []
    for i in string:
        if i == "'":
            for j in range(string.index(i)+1, len(string)):
                if string[j] == "'":
                    del string[string.index(i):j+1]
                    break
        if i == '(':
            check += [i]
        elif i == ')':
            if check and check[-1] == '(':
                check.pop(-1)
            else:
                check.append(i)
        elif i == '{':
            check += [i]
        elif i == '}':
            if check and check[-1] == '{':
                check.pop(-1)
            else:
                check.append(i)
        elif i == '[':
            check += [i]
        elif i == ']':
            if check and check[-1] == '[':
                check.pop(-1)
            else:
                check.append(i)

    if check:
        print('#{} 0'.format(t+1))
    else:
        print('#{} 1'.format(t+1))

