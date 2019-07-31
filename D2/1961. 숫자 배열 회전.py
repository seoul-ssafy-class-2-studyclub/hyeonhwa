def ret(a):
    re_a = [[a[i][j] for i in range(len(a))]for j in range(len(a))]
    for i in range(len(re_a)):
        re_a[i].reverse()
    return re_a

T = int(input())
for t in range(T):
    N = int(input())
    n, l = [], []
    for i in range(N):
        n.append(list(input().split()))
    n1 = ret(n)
    n2 = ret(n1)
    n3 = ret(n2)
    print('#{}'.format(t+1))
    for j in range(len(n)):
        print('{} {} {}'.format(''.join(n1[j]), ''.join(n2[j]), ''.join(n3[j])))