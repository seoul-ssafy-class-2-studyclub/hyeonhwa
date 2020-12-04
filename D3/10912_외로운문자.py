for t in range(int(input())):
    st = [i for i in input()]
    st.sort()
    res = []
    while st:
        x = st.pop(0)
        if st and x == st[0]:
            st.pop(0)
        else:
            res.append(x)
    if res:
        res = ''.join(list(sorted(res)))
    else:
        res = 'Good'
    print(f'#{t+1} {res}')
