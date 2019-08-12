for t in range(1):
    N = int(input())
    codes = [i for i in input().split()]
    command = int(input())
    commands = [i for i in input().split()]
    for i in range(len(commands)):
        if commands[i] == 'I':
            k = int(commands[i+1])
            for j in range(i+3, i+3+int(commands[i+2])):
                codes.insert(k, commands[j])
                k += 1
    print('#{} {}'.format(t+1, ' '.join(codes[:10])))