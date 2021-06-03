import heapq

n = int(input())
heap = []
res = []
for _ in range(n):
    x = int(input())
    if len(heap) == 0 and x == 0:
        res.append(0)
    elif x != 0:
        heapq.heappush(heap, x)
    elif len(heap) and x == 0:
        res.append(heapq.heappop(heap))
print('\n'.join(list(map(str, res))))