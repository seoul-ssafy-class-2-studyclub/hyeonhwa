def pal(a):
    if a == a[::-1]:
        return True
    else:
        return False

for t in range(1):
    N, l = input().split()
    l = list(l)
    for k in range(2, len(l), 2):
        for i in l:
            if pal(l[l.index(i):l.index(i)+k]):
                print(l[l.index(i):l.index(i)+k])
                del l[l.index(i):l.index(i)+k]
                
    print(l)