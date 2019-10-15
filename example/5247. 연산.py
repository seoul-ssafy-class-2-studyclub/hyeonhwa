from collections import deque

def cal(a, x):
    if x == 1:
        return a+1
    if x == 2:
        return a-1
    if x == 3:
        return a*2
    if x == 4:
        return a-10


def cals(n):
    queue = deque()
    queue.append(n)
    cnt = 1
    while queue:
        for i in range(len(queue)):
            x = queue.popleft()
            for i in range(1, 5):
                y = cal(x, i)
                if y != N and 0 <= y <= M*2:
                    if not visited[y]:
                        visited[y] = cnt
                        queue.append(y)
        cnt += 1
        if visited[M]:
            return


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    visited = [0 for _ in range(M*2+1)]
    cals(N)
    print('#{} {}'.format(t+1, visited[M]))
