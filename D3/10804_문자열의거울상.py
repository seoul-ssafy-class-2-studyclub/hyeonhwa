mirror = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}

for t in range(int(input())):
    st = input()
    res = ''
    for i in range(len(st)-1, -1, -1):
        res += mirror[st[i]]
    print(f'#{t+1} {res}')