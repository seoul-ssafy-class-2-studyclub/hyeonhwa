import sys
from collections import deque

sys.setrecursionlimit(1000000)
'''
# Cycle 유무 찾기
# 일반적 방법 O(V(V+E))
def findCycle(start, here):
    if visited[here]:
        if here == start:
            return True
        return False
    visited[here] = True
    for there in node[here]:
        if findCycle(start, there):
            return true
    return false
    
# 개선 O(V+E)
# visited: -1 -> dfs 끝 X / 1 dfs 끝
def findCycle(here):
    if visited[here]:
        if visited[here] == -1:
            return True
        return False
    visited[here] = -1
    for there in node[here]:
        if findCycle(there):
            return True
    visited[here] = 1
    return False
'''
import sys
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(node, past):
    if visited[node] == 1:
        return node
    
    visited[node] = 1

    for nxt in l[node]:
        if nxt == past:
            continue
        res = dfs(nxt, node)
        if res == -2:
            return -2
        if res >= 0:
            visited[node] = 2
            if node == res:
                return -2
            else:
                return res
    return -1

# input = sys.stdin.readline
# N = int(input())
# adj = [[] for _ in range(N + 1)]
# chk = [False] * (N + 1)

# for i in range(N):
#     s1, s2 = map(int, input().split())
#     adj[s1].append(s2)
#     adj[s2].append(s1)

# dfs(1, 0)
# queue = deque()
# res = [-1] * (N + 1)
# for i in range(1, N + 1):
#     if chk[i] == 2:
#         res[i] = 0
#         queue.append(i)

# while queue:
#     node = queue.popleft()
#     for nxt in adj[node]:
#         if res[nxt] == -1:
#             res[nxt] = res[node] + 1
#             queue.append(nxt)

# print(' '.join(map(str, res[1:])))

def bfs():
    queue = deque()
    for i in range(1, N+1):
        if visited[i] == 2:
            res[i] = 0
            queue.append(i)
    while queue:
        x = queue.popleft()
        for i in l[x]:
            if res[i] == -1:
                res[i] = res[x]+1
                queue.append(i)


N = int(input())
station = [0 for _ in range(N+1)]
l = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(N):
    x, y = map(int, input().split())
    l[x].append(y)
    l[y].append(x)
dfs(1, 0)
# print(visited)    
res = [-1] * (N+1)
bfs()
print(' '.join(map(str, res[1:])))