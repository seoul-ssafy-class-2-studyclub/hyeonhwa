def name(a):
    cnt = 0
    for i in a:
        for j in i:
            if j.isdigit():
                a.remove(i)
                break
    for i in a:
        if i[0].isupper() and i[1:].islower():
            cnt += 1
        if len(i) == 1 and i.isupper():
            cnt += 1
    return cnt

T = int(input())
for t in range(T):
    N = int(input())
    n = input().split()
    replaces = ['.', '!', '?']
    l = []
    for i in n[:]:
        for replace in replaces:
            if replace in i:
                n[n.index(i)] = i = i.replace(replace,'')
                l.append(n[:n.index(i)+1])
                del n[:n.index(i)+1]
    print('#{}'.format(t+1), end=' ')
    for i in l:
        if i != l[-1]:
            print(name(i), end=' ')
        else:
            print(name(i))