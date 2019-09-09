def check(arr, start):
    global res
    arr.append(start)
    if road[arr[-1]] == []:
        # arr.pop()
        return 0
    for x in road[arr[-1]]:
        if x not in arr:
            if res < len(arr):
                res = len(arr)
            check(arr, x)
            arr.pop()



T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    road = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        road[x].append(y)
        road[y].append(x)
    mroad = 0
    for start in range(0, N+1):
        res = 0
        check([], start)
        if mroad < res+1:
            mroad = res+1
    print('#{} {}'.format(t+1, mroad))