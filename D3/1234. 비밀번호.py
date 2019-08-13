def pal(a):
    if len(a) == 0 or len(a) == 1:
        return True
    if a[0] != a[-1]:
        return False
    else:
        a.pop(0)
        a.pop(-1)
        return pal(a)

def rep(l):
    for k in range(n, 0, -2):
        for i in range(len(l)):
            if pal(l[i:i+k]) and len(l[i:i+k]) == k:
                del l[i:i+k]
    return l


for t in range(1):
    N, l = input().split()
    l = list(l)
    if int(N)%2:
        n = int(N)-1
    else:
        n = int(N)
    
    while l:
        l = rep(l)
        if l == rep(l):
            break
    print(l)     
    # print('#{} {}'.format(t+1, ''.join(l)))