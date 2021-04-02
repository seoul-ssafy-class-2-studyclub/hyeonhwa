n, r, c = map(int, input().split())
res = 0
s, e = 0, 0
n -= 1
while n >= 0:
    # 1
    if r < s + 2**n and c < e + 2**n:
        if not n:
            res += 1
    # 2
    elif r < s + 2**n and c >= e + 2**n:
        e += 2**n
        if n:
            res += 4**n
        else:
            res += 2
    # 3
    elif r >= s + 2**n and c < e + 2**n:
        s += 2**n
        if n:
            res += 2*4**n
        else:
            res += 3
    # 4
    else:
        s += 2**n
        e += 2**n
        if n:
            res += 3*4**n
        else:
            res += 4
    n -= 1
print(res-1)
