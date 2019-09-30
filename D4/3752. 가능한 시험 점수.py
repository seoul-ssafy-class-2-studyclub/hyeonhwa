T = int(input())
for t in range(T):
    N = int(input())
    score = list(map(int, input().split()))
    res = [0 for _ in range(sum(score)+1)]
    visited = [0]
    for s in score:
        temp = visited[:]
        for i in temp:
            if not res[i+s]:
                res[i+s] = 1
                visited.append(i+s)
    print('#{} {}'.format(t+1, sum(res)+1))
