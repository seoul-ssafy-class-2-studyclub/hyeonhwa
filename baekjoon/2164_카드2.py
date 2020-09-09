import sys
from queue import deque
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
queue = deque()
for i in range(1, n+1):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])
