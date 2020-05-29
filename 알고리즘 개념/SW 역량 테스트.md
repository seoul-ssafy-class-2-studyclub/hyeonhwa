# SW 역량 테스트



### 부분집합

```python
for i in range(1<<len(A)):
        a = []
        for j in range(len(A)):
            if i & (1<<j):
                a.append(A[j])
```



### backtracking

```python
def backtrack(arr, x):
    global res
    if sum(arr) >= res:
        return
    if len(arr) == N:
        if res > sum(arr):
            res = sum(arr)
        return
    for i in range(N):
        if i not in visited:
            arr.append(board[x][i])
            visited.append(i)
            backtrack(arr, x+1)
            arr.pop()
            visited.pop()
```



### 프림

```python
INF = float('inf')
cost = [INF]*cnt
cost[2] = 0
visit = [False]*cnt
queue = []
heapq.heappush(queue, (0, 2))
while queue:
    value, node = heapq.heappop(queue)
    visit[node] = True
    for n, v in near[node]:
        if visit[n]:
            continue
        if cost[n] > v:
            cost[n] = v
            heapq.heappush(queue, (v, n))
if INF in cost[2:]:
    print(-1)
else:
    print(sum(cost[2:]))
```



### 다익스트라

```python
import heapq

def solve():
    length = [1000000 for _ in range(N+1)]
    length[0] = 0
    priority_queue = []
    heapq.heappush(priority_queue, 0)
    while priority_queue:
        loc = heapq.heappop(priority_queue)
        for nxt_loc, l in nodes[loc].items():
            nxt_length = length[loc] + l
            if nxt_length < length[nxt_loc]:
                length[nxt_loc] = nxt_length
                heapq.heappush(priority_queue, nxt_loc)
    return length


T = int(input())
for t in range(T):
    N, E = map(int, input().split())
    nodes = [{} for _ in range(N+1)]
    for _ in range(E):
        v, u, w = map(int, input().split())
        if u in nodes[v]:
            nodes[v][u] = min(nodes[v][u], w)
        else:
            nodes[v][u] = w
    res = solve()
    print('#{} {}'.format(t+1, res[-1]))
```



### kruskal

```python
# Kruskal's Algorithm
parent = {}
rank = {}

# 정점을 독립적인 집합으로 만듦
def make_set(v):
    parent[v] = v
    rank[v] = 0

# 해당 정점의 최상위 정점을 찾음
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

# 두 정점 연결
def union(v, u):
    root1 = find(v)
    root2 = find(u)
    if root1 != root2:
        if rank[root1] > rank[root2]: # 짧은 트리 -> 긴 트리 가리키게 함
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal():
    for v in range(V+1):
        make_set(v)
    mst = 0
    for v, u, w in nodes:
        if find(v) != find(u):
            union(v, u)
            mst += w
    return mst


T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(E)]
    nodes.sort(key=lambda x:x[2])
    res = kruskal()
    print('#{} {}'.format(t+1, res))
```



### queue

```python
import collections

def grow(x, y):
    board[x][y] = cnt
    queue = collections.deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in idx:
            if 0 <= x+dx < N and 0 <= y+dy < M and board[x+dx][y+dy] == 1:
                board[x+dx][y+dy] = cnt
                queue.append((x+dx, y+dy))
```



### 윷놀이

```python
def bfs(score, n):
    global res
    if n == 10:
        res = max(res, sum(score))
        return
    for i in range(4):
        if visited[i] != 32:
            dice = nums[n]
            if board[visited[i]][dice] == 32:
                temp = visited[i]
                visited[i] = 32
                # print(visited)
                bfs(score, n+1)
                visited[i] = temp
            elif board[visited[i]][dice] not in visited:
                temp = visited[i]
                visited[i] = board[visited[i]][dice]
                # print(visited)
                score[i] += board[visited[i]][0]
                bfs(score, n+1)
                score[i] -= board[visited[i]][0]
                visited[i] = temp
            else:
                continue
```



### 순열 / 조합

```python
def perm(n, arr):
    if len(arr) == n:
        print(arr)
        return
    for i in range(n):
        if visit[i]:
            continue
        visit[i] = True
        perm(n, arr+[i])
        visit[i] = False
def comb(arr, idx):
    if len(arr) == n:
        print(arr)
        return
    for i in range(idx+1, n):
        comb(arr+[i], i)

n = 3
visit = [False]*n
# perm(n, [])
comb([], -1)
```



### dp

```python
l = [list(map(int, input().split())) for _ in range(N)]
dp = [0]*(N)
for i in range(N):
    for j in range(i+1):
        if l[i - j][0] <= j and i + l[i][0] <= N:
            dp[i] = max(dp[i], dp[i-j]+l[i][1])
    if dp[i] == 0 and i + l[i][0] <= N:
        dp[i] = l[i][1]
```



### 마름모(대각선 사각형)

```python
def eat(i,j):
    global res
    start, end = i,j
    ate, k = [], 3
    while True:
        dx, dy = idx[k]
        x = i+dx
        y = j+dy
        if 0 <= x < p and 0 <= y < p:
            if not pos[x][y] in ate:
                i, j = x, y
                ate.append(pos[x][y])
                if x == start and y == end:
                    if res < len(ate):
                        res = len(ate)
                    return
            else:
                return
        elif y == -1:
            k = 0
        elif x == p:
            k = 2
        elif y == p:
            k = 1


for t in range(int(input())):
    N = int(input())
    dessert = [list(map(int,input().split())) for _ in range(N)]
    idx = [(-1, 1), (1, -1), (-1, -1), (1, 1)]
    res = 0
    for p in range(N,2,-1):
        for q in range(N-p+1):
            for i in range(N-p+1):
                pos = [0]*p
                for j in range(p):
                    pos[j]=dessert[j+q][i:i+p]
                for y in range(1, p-1):
                    eat(0, y)
                    if res:
                        break
                if res:
                    break
            if res:
                break
        if res:
            break
    if res == 0:
        res = -1
    print('#{} {}'.format(t+1, res))
```





### 하드코딩 -> index 주의