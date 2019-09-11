def dfs(arr):
    if arr and arr[0] == arr[-1]:
        res.append() 
        return
    for i in roads:
        if i not in arr:
            arr.append(i)
            dfs(arr)
            arr.pop()


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    roads = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, c = map(int, input().split())
        roads[s].append((e, c))
    res = []
    dfs([])
