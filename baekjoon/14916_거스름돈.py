import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
res = 0
while n%5:
    if n == 1:
        break
    n -= 2
    res += 1
if n == 1:
    print(-1)
else:
    print(res + n//5)