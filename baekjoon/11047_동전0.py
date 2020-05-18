n, k = map(int, input().split())
values = [int(input()) for _ in range(n)]
res = 0
for i in range(n-1, -1, -1):
    if k == 0:
        break
    if k < values[i]:
        continue
    res += k // values[i]
    k %= values[i]
print(res)