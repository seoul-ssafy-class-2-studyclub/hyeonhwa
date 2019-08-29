def length(arr, x, y):
    r = abs(arr[x][0] - arr[y][0]) + abs(arr[x][1] - arr[y][1])
    return r


def find(customer, r_sum=0, res=[0]):
    global m_sum
    if len(res) == len(customer):
        if m_sum > r_sum:
            m_sum = r_sum
            m_sum += abs(customer[res[-1]][0]-end[0]) + abs(customer[res[-1]][1]-end[1])
        return 1
    else:
        for i in range(len(customer)):
            if i not in res:
                res.append(i)
                r_sum += length(customer, res[-2], res[-1])
                if r_sum > m_sum:
                    r_sum -= length(customer, res[-2], res[-1])
                    res.pop()
                    continue
                find(customer, r_sum, res)
                r_sum -= length(customer, res[-2], res[-1])
                res.pop()


T = int(input())
for t in range(T):
    N = int(input())
    l = list(map(int, input().split()))
    customer = []
    s_e = []
    for i in range(0, len(l), 2):
        s_e.append(l[i:i+2])
    end = s_e[1]
    customer = [i for i in s_e if s_e.index(i) != 1]
    m_sum = 1000000000
    find(customer)
    print(m_sum)
# a = [i+1 for i in range(101)]
# from itertools import permutations
# per = permutations(a,100)
# print(list(per))

# 순열
# def perm(n, res=[0]):
#     if len(res) == n+1:
#         # rs.append(res)
#         print(res)
#     else:
#         for i in range(n):
#             if visited[i]:
#                 continue
#             res.append(i)
#             visited[i] = 1
#             perm(n, res)
#             visited[i] = 0
#             res.pop()
                

# visited = [1]
# visited += [0 for _ in range(N)]