def pal(x):
    i, j = 0, len(x)-1
    while i < j:
        if x[i] != x[j]:
            return 0
        i += 1
        j -= 1
    return 1


for t in range(int(input())):
    st = input()
    res = pal(st)
    print(f'#{t+1} {res}')
