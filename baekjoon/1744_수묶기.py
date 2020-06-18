import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
minus = []
plus = []
zero = []
res = 0
for _ in range(n):
    x = int(input())
    if x < 0:
        minus.append(x)
    elif x > 1:
        plus.append(x)
    elif x == 1:
        res += 1
    elif x == 0:
        zero.append(x)
minus.sort()
plus.sort(reverse=True)
for i in range(0, len(minus), 2):
    if i != len(minus)-1:
        res += minus[i]*minus[i+1]
    else:
        if not zero:
            res += minus[i]
        if zero:
            zero.pop()
for i in range(0, len(plus), 2):
    if i != len(plus)-1:
        res += plus[i]*plus[i+1]
    else:
        res += plus[i]
print(res)