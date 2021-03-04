x, y, z = map(int, input().split())
# l, p, v
res = 0
i = 1
while True:
    if x+y+z == 0:
        break
    if z >= y:
        res += x
        z -= y
    else:
        if z > x:
            res += x
        else:
            res += z
        print(f"Case {i}: {res}")
        x, y, z = map(int, input().split())
        res = 0
        i += 1
