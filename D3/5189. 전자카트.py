# from pprint import pprint
def find(arr, num, r_sum=0, road=[0]):
    # global r_sum
    global m_sum
    if len(road) == num:
        r_sum += arr[road[-1]][0]
        if r_sum < m_sum:
            m_sum = r_sum
        return 1
    for i in range(num):
        if i not in road:
            road.append(i)
            r_sum += arr[road[-2]][road[-1]]
            if r_sum > m_sum:
                r_sum -= arr[road[-2]][road[-1]]
                road.pop()
                continue
            find(arr, num, r_sum, road)
            r_sum -= arr[road[-2]][road[-1]]
            road.pop()


T = int(input())
for t in range(T):
    N = int(input())
    n = [list(map(int, input().split())) for _ in range(N)]
    m_sum = 10000000000
    find(n, N)
    print('#{} {}'.format(t+1, m_sum))