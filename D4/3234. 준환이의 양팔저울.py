def per(arr):
    global res
    if len(arr) <= N:
        if len(arr) == N:
            res.append(arr)
            return
        for i in range(N):
            if visit[i] == False:
                visit[i] = True
                per(arr+[weights[i]])
                visit[i] = False


T = int(input())
for t in range(T):
    N = int(input())
    weights = list(map(int, input().split()))
    cnt = 0
    visit = [False] * N
    res = []
    per([])
    for x in res:
        for i in range(1<<N):
            left, right = [], []
            for j in range(N):
                if i & (1<<j):
                    left.append(x[j])
                else:
                    right.append(x[j])
                if sum(left) < sum(right):
                    break
            if sum(left) >= sum(right) and len(left) + len(right) == N:
                cnt += 1
    print(cnt)
