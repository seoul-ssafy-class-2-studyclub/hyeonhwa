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
    