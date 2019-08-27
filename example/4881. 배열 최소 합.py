def change(arr, k=0, r_sum=0, rs=[]):
    global m_sum
    if len(rs) == N:
        if m_sum > r_sum:
            m_sum = r_sum
        return 0
    for i in range(N):
        if i not in rs:
            rs.append(i)
            r_sum += arr[k][i]
            if r_sum > m_sum:
                rs.pop()
                r_sum -= arr[k][i]
                continue
            change(arr, k+1, r_sum, rs)
            rs.pop()
            r_sum -= arr[k][i]
        

for T in range(int(input())):
    N = int(input())
    n = []
    rs = []
    m_sum = 10000000
    for i in range(N):
        n.append(list(map(int, input().split())))
    change(n)
    print('#{} {}'.format(T+1, m_sum))
