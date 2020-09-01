import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
weights = [int(input()) for _ in range(n)]
weights.sort()

res = 0
num = n
for weight in weights:
    res = max(res, weight*num)
    num -= 1
print(res)