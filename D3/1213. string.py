for t in range(1):
    N = int(input())
    search = input()
    strings = [i for i in input()]
    result = []
    for i in range(len(strings)):
        if strings[i] == search[0]:
            n = ''.join(strings[i:i+len(search)])
            result.append(n)
    print('#{} {}'.format(t+1,result.count(search)))
