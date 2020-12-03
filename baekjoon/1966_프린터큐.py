for _ in range(int(input())):
    n, m = map(int, input().split())
    enum = list(enumerate(list(map(int, input().split()))))
    res = 0
    while True:
        if not enum:
            break
        idx, value = enum.pop(0)
        if enum and max(enum, key=lambda x:x[1])[1] > value:
            enum.append((idx, value))
        else:
            res += 1
            if m == idx:
                print(res)
                break
