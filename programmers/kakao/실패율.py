def solution(N, stages):
    touch = [0]*(N+1)
    no_clear = [0]*(N+1)
    for i in stages:
        for j in range(i):
            touch[j] += 1
        no_clear[i-1] += 1
    res = [0]*N
    for i in range(N):
        if touch[i]:
            res[i] = (no_clear[i]/touch[i], i+1)
        else:
            res[i] = (0, i+1)
    res.sort(key=lambda x:x[0], reverse=True)
    res = [i[1] for i in res]
    return res

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
