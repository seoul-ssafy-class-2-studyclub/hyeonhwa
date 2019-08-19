T = int(input())
for t in range(T):
    s = input()
    res = []
    for i in s:
        if not res:
            res.append(i)
        elif res[-1] != i:
            res.append(i)
        elif res[-1] == i:
            res.pop(-1)
    print('#{} {}'.format(t+1, len(res)))
