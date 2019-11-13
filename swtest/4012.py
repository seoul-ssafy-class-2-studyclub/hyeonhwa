def comb(arr, idx):
    global A
    global B
    global res
    if len(arr) == n:
        A, B = 0, 0
        arrb = [i for i in range(N) if i not in arr]
        resa([], arr)
        resb([], arrb)
        if abs(A-B) < res:
            res = abs(A-B)
        return
    for i in range(idx+1, N):
        if i not in arr:
            comb(arr+[i], i)


def resa(arr, l):
    global A
    if len(arr) == 2:
        A += food[arr[0]][arr[1]]
        return
    for i in range(n):
        if visita[i] == False:
            visita[i] = True
            resa(arr+[l[i]], l)
            visita[i] = False


def resb(arr, l):
    global B
    if len(arr) == 2:
        B += food[arr[0]][arr[1]]
        return
    for i in range(n):
        if visitb[i] == False:
            visitb[i] = True
            resb(arr+[l[i]], l)
            visitb[i] = False


T = int(input())
for t in range(T):
    N = int(input())
    food = [list(map(int, input().split())) for _ in range(N)]
    n = N//2
    A, B = 0, 0
    visita = [False]*n
    visitb = [False]*n
    res = 987654321
    comb([], -1)
    print(f'#{t+1} {res}')
