for t in range(int(input())):
    n = int(input())
    res = 0
    for x in range(1, n+1):
        if x%2:
            res += x
        else:
            res -= x
    print(f'#{t+1} {res}')