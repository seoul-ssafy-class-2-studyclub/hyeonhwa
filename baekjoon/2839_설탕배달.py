import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

res = 0
while n%5:
    n -= 3
    res += 1
    if n < 3:
        break
if 0 < n < 3:
    print(-1)
else:
    print(res+n//5)