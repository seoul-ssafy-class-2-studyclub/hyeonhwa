import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

res = [0, 0, 0]
res[0] = t//300
t %= 300
res[1] = t//60
t %= 60
res[2] = t//10
if t%10:
    res = -1
else:
    res = ' '.join(list(map(str, res)))
print(res)