import heapq

def di(x, board):
    length = [1e10]*(n+1)
    length[x] = 0
    queue = []
    heapq.heappush(queue, (0, x))
    while queue:
        value, node = heapq.heappop(queue)
        for nxt_n, nxt_v in board[node].items():
            nxt = nxt_v + value
            if length[nxt_n] > nxt:
                length[nxt_n] = nxt
                heapq.heappush(queue, (nxt, nxt_n))
    return length


n, m, d = map(int, input().split())
city = [{} for _ in range(n+1)]
rev_city = [{} for _ in range(n+1)]
for _ in range(m):
    u, v, t = map(int, input().split())
    city[u][v] = t
    rev_city[v][u] = t
l1 = di(d, city)
l2 = di(d, rev_city)
res = 0
for i in range(1, n+1):
    res = max(res, l1[i] + l2[i])
print(res)
