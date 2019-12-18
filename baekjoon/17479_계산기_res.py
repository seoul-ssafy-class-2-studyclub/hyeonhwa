N = int(input())
res = []
while N:
    if N & 1:
        res.append('[/]')
        N *= 2
    elif N & 2:
        res.append('[+]')
        N -= 2
    else:
        res.append('[*]')
        N //= 2
if not res:
    print(-1)
else:
    print(len(res))
    print(' '.join(res[::-1]))
