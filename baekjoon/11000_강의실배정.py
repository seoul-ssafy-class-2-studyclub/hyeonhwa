import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

# 우선순위큐
n = int(input())
subject = [list(map(int,input().split())) for _ in range(n)]
subject.sort(key=lambda x:x[0])
finish = []
heapq.heappush(finish, subject[0][1])
for s, t in subject[1:]:
    if finish[0] <= s:
        heapq.heappop(finish)
    heapq.heappush(finish, t)
print(len(finish))