import sys
sys.stdin = open('input.txt', 'r')

def bfs(arr, start):
    visited = []
    queue = [start]
    while queue:
        result = []
        for i in queue:
            if i not in visited:
                result.extend(callbook[i])
                visited.append(i)
                for j in result[:]:
                    if j in visited:
                        result.remove(j)
        if len(result) == 0:
            return queue
        else:
            queue = result


for t in range(10):
    n, s = map(int, input().split())
    l = list(map(int, input().split()))
    callbook = [[] for _ in range(max(l)+1)]
    for i in range(0, len(l), 2):
        callbook[l[i]].append(l[i+1])
    res = bfs(callbook, s)
    print('#{} {}'.format(t+1, max(res)))
