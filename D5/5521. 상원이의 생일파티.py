from collections import deque

def close(x=1):
    global res
    cnt = 0
    queue = deque()
    queue.append(x)
    nxt = deque()
    while queue:
        x = queue.popleft()
        if visit[x] == False:
            visit[x] = True
            nxt.extend(friends[x])
        if not queue:
            queue = nxt
            for i in nxt:
                if i != 1:
                    res.add(i)
            nxt = deque()
            cnt += 1
            if cnt == 2:
                break


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    friends = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a] += [b]
        friends[b] += [a]
    visit = [False for _ in range(N+1)]
    res = set()
    close()
    print('#{} {}'.format(t+1, len(res)))