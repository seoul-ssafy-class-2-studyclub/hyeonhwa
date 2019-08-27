def change(arr):
    res = []
    stack = []
    for i in arr:
        if i == '+' or i == '-' or i == '*' or i == '/' or i == '(':
            if i == '(' or not stack:
                stack.append(i)
            else:
                if dic[stack[-1]] > dic[i]:
                    while dic[stack[-1]] >= dic[i]:
                        res.append(stack.pop())
                    stack.append(i)
                else:
                    stack.append(i)
        elif i == ')':
            p = stack.pop()
            while p != '(':
                res.append(p)
                p = stack.pop()
        else:
            res.append(int(i))
    while stack:
        res.append(stack.pop())
    return res


def cals(arr):
    cals = []
    for i in arr:
        if type(i) == int:
            cals.append(i)
        else:
            if i == '+':
                cals.append(cals.pop()+cals.pop())
            elif i == '-':
                cals.append(cals.pop(-2)-cals.pop())
            elif i == '*':
                cals.append(cals.pop()*cals.pop())
            else:
                cals.append(cals.pop(-2)/cals.pop())
    return cals[-1]



for t in range(10):
    N = int(input())
    eq = [i for i in input()]

    dic = {
        '+' : 1,
        '-' : 1,
        '*' : 2,
        '/' : 2,
        '(' : 0,
    }
    change_eq = change(eq)
    print(change_eq)
    print('#{} {}'.format(t+1, cals(change_eq)))

