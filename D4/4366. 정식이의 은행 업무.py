def change2(x):
    res = 0
    j = 1
    for i in range(len(x)-1, -1, -1):
        res += x[i] * j
        j *= 2
    return res


def change3(x):
    res = 0
    j = 1
    for i in range(len(x)-1, -1, -1):
        res += x[i] * j
        j *= 3
    return res


def c2(x):
    res2 = []
    for i in range(len(x)):
        if x[i] == 1:
            x[i] = 0
            rex = change2(x)
            res2.append(rex)
            x[i] = 1
        else:
            x[i] = 1
            rex = change2(x)
            res2.append(rex)
            x[i] = 0
    return res2


def c3(x):
    res3 = []
    for i in range(len(x)):
        if x[i] == 0:
            x[i] = 1
            rex = change3(x)
            res3.append(rex)
            x[i] = 2
            rex = change3(x)
            res3.append(rex)
            x[i] = 0
        elif x[i] == 1:
            x[i] = 0
            rex = change3(x)
            res3.append(rex)
            x[i] = 2
            rex = change3(x)
            res3.append(rex)
            x[i] = 1
        else:
            x[i] = 0
            rex = change3(x)
            res3.append(rex)
            x[i] = 1
            rex = change3(x)
            res3.append(rex)
            x[i] = 2
    return res3


T = int(input())
for t in range(T):
    x1 = [int(i) for i in input()]
    x2 = [int(i) for i in input()]
    l1 = c2(x1)
    l2 = c3(x2)
    x = [i for i in l1 if i in l2]
    print('#{} {}'.format(t+1, x[0]))