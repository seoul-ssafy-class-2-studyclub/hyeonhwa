T = int(input())
for t in range(T):
    stack = []
    eq = [_ for _ in input().split()]
    try:
        for i in eq:
            if i == '+':
                stack.append(stack.pop()+stack.pop())
            elif i == '-':
                stack.append(stack.pop(-2)-stack.pop())
            elif i == '*':
                stack.append(stack.pop()*stack.pop())
            elif i == '/':
                stack.append(int(stack.pop(-2)/stack.pop()))
            elif i == '.' and len(stack) == 1:
                print('#{} {}'.format(t+1, stack[-1]))
            elif i == '.' and len(stack) > 1:
                print('#{} error'.format(t+1))
            else:
                stack.append(int(i))
    except:
        print('#{} error'.format(t+1))
