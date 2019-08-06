def cycle(a):
    value = 1
    for i in a[:5]:
        if i - value <= 0:
            a.insert(len(a), 0)
            a.remove(i)
            break
        else:
            a.insert(len(a),(i - value))
            a.remove(i)
        value += 1
    return a
    
for t in range(10):
    N = int(input())
    password = list(map(int, input().split()))
    while True:
        password = cycle(password)
        if password[-1] == 0:
            break
    print('#{} {}'.format(t+1, ' '.join(list(map(str, password)))))
