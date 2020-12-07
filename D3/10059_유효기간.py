for t in range(int(input())):
    st = input()
    a = int(st[:2])
    b = int(st[2:])
    flag1, flag2 = 0, 0
    if 0 < a <= 12:
        flag1 = 1
    if 0 < b <= 12:
        flag2 = 1
    if flag1 and flag2:
        res = 'AMBIGUOUS'
    elif flag1:
        res = 'MMYY'
    elif flag2:
        res = 'YYMM'
    else:
        res = 'NA'
    print(f'#{t+1} {res}')
