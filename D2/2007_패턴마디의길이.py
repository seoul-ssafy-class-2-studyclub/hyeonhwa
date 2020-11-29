for t in range(int(input())):
    st = input()
    pat = ''
    for i in range(len(st)):
        if not pat:
            pat += st[i]
            continue
        if st[i] == pat[0]:
            if st[i:i+len(pat)] == pat:
                print(f'#{t+1} {len(pat)}')
            else:
                pat += st[i]
        else:
            pat += st[i]
            