for _ in range(int(input())):
    s = input()
    st = []
    for i in s:
        if i == '(':
            st.append(i)
        else:
            if st:
                st.pop()
            else:
                print('NO')
                break
    else:
        if st:
            print('NO')
        else:
            print('YES')