def nqueen(arr, N):
    global cnt
    if len(arr) == N:
        cnt += 1
        return 0
    s = [i for i in range(N)]
    for i in range(len(arr)):
        if arr[i] in s:
            s.remove(arr[i])
        check = len(arr) - i
        if arr[i] + check in s:
            s.remove(arr[i]+check)
        if arr[i] - check in s:
            s.remove(arr[i]-check)
    if s:
        for i in s:
            arr.append(i)
            nqueen(arr, N)
            arr.pop()

T = int(input())
for t in range(T):
    N = int(input())
    cnt = 0
    nqueen([], N)
    print('#{} {}'.format(t+1, cnt))