def city(x):
    queue = [x]
    while queue:
        a = queue.pop(0)
        if not visited[a]:
            visited[a] = True
            queue.extend(board[a])


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    visited = [False for _ in range(N+1)]
    board = [[] for _ in range(N+1)]
    for _ in range(M):
        n, m = map(int, input().split())
        board[n] += [m]
        board[m] += [n]
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            city(i)
            cnt += 1
    print('#{} {}'.format(t+1, cnt))
