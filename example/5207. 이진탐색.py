def binary(l, r, check=''):
    global cnt
    m = (l+r)//2
    if n[m] == x:
        cnt += 1
        return True
    if n[m] > x and (not check or check == 'r'):
        return binary(l, m-1, 'l')
    elif n[m] < x and (not check or check == 'l'):
        return binary(m+1, r, 'r')


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    n = list(map(int, input().split()))
    n.sort()
    m = list(map(int, input().split()))
    cnt = 0
    for x in m:
        binary(0, len(n)-1)
    print(f'#{t+1} {cnt}')
