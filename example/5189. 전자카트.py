def perm(arr, s):
    global res
    if s >= res:
        return
    if len(arr) == N:
        s += board[arr[-1]][0]
        if res > s:
            res = s
        return
    for i in range(N):
        if i not in arr:
            arr.append(i)
            perm(arr, s+board[arr[-2]][arr[-1]])
            arr.pop()


T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    res = 100000000
    perm([0], 0)
    print('#{} {}'.format(t+1, res))
