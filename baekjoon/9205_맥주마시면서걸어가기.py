import sys
input = lambda: sys.stdin.readline().rstrip()

def mst():
    q = []
    q.append(0)
    visit = [False]*(n+2)
    while q:
        node = q.pop()
        if visit[node]:
            continue
        visit[node] = True
        x1, y1 = loc[node]
        for i in range(n+2):
            if not visit[i]:
                x2, y2 = loc[i]
                if abs(x1 - x2) + abs(y1 - y2) <= 1000:
                    q.append(i)
        if visit[-1]:
            return 'happy'
    return 'sad'


res = []
for tc in range(int(input())):
    n = int(input())
    loc = [list(map(int, input().split())) for _ in range(n+2)]
    res.append(mst())
print('\n'.join(res))
