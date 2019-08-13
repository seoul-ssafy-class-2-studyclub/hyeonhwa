def pal(a):
    if len(a) == 0 or len(a) == 1:
        return True
    if a[0] != a[-1]:
        return False
    else:
        a.pop(0)
        a.pop(-1)
        return pal(a)

# def pal(a):
#     if n == 0 or n == 1:
#         return True
#     if a[0] != a[-1]:
#         return False
#     else:
#         a.pop(0)
#         a.pop(-1)
#         return pal(a)

T = int(input())
for t in range(T):
    N, M = input().split()
    pallist = [[n for n in input()] for i in range(int(N))]
    for i in pallist:
        for j in range(len(i)):
            if pal(i[j:j+int(M)]) and len(i[j:j+int(M)]) == int(M):
                print('#{} {}'.format(t+1, ''.join(i[j:j+int(M)])))
    pallist2 = list(map(list, zip(*pallist)))
    for i in pallist2:
        for j in range(len(i)):
            if pal(i[j:j+int(M)]) and len(i[j:j+int(M)]) == int(M):
                print('#{} {}'.format(t+1, ''.join(i[j:j+int(M)])))

