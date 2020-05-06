def solution(n, lost, reserve):
    visit = [0]*(n+1)
    for i in range(1, n+1):
        if i in lost and i in reserve:
            visit[i] = 1
        elif i in lost and i not in reserve:
            if i-1 > 0 and i-1 in reserve and i-1 not in lost and visit[i-1] == 0:
                visit[i] = 1
                visit[i-1] = 1
            elif i+1 <= n and i+1 in reserve and i+1 not in lost and visit[i+1] == 0:
                visit[i] = 1
                visit[i+1] = 1
        elif i not in lost and i not in reserve:
            visit[i] = 1
    for i in reserve:
        visit[i] = 1
    return visit.count(1)

solution(5, [2, 4], [3])