res = 0
p = 0
for _ in range(4):
    x, y = map(int, input().split())
    p += y-x
    res = max(p, res)
print(res)