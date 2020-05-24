import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
crane = list(map(int, input().split()))
crane.sort(reverse=True)
m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)
boxes = deque(boxes)
num = []
temp = []
res = 0
if boxes[0] > crane[0]:
    print(-1)
else:
    while boxes or temp:
        if not boxes and len(num) != n:
            num.clear()
            res += 1
            boxes.extendleft(reversed(temp))
            temp.clear()
        if len(num) == n:
            res += 1
            num.clear()
            boxes.extendleft(reversed(temp))
            temp.clear()
        if crane[len(num)] >= boxes[0]:
            num.append(boxes.popleft())
        else:
            temp.append(boxes.popleft())
    print(res + 1)