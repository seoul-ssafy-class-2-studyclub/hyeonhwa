for t in range(int(input())):
    n = int(input())
    st = ''
    for _ in range(n):
        x, y = input().split()
        st += x*int(y)
    print(f'#{t+1}')
    for i in range(0, len(st), 10):
        print(st[i:i+10])
