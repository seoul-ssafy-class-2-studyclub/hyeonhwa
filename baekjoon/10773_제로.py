k = int(input())
res = []
for _ in range(k):
    last = int(input())
    if last != 0:
        res.append(last)
    else:
        res.pop()
print(sum(res))