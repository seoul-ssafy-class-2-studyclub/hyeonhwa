from pprint import pprint
# import collections

def down():
    for i in range(1, N+1):
        y = i
        for j in range(1, H+1):
            if visit[j][y]:
                y += 1
            elif visit[j][y-1]:
                y -= 1
        if y != i:
            return 0
    return 1


def newline(idx, cnt):
    global res
    if cnt > 3:
        return
    if down():
        res = min(res, cnt)
        return
    for i in range(idx, H+1):
        for j in range(1, N):
            if visit[i][j]:
                continue
            if visit[i][j-1]:
                continue
            if visit[i][j+1]:
                continue
            visit[i][j] = True
            newline(i, cnt+1)
            visit[i][j] = False


N, M, H = map(int, input().split())
visit = [[False]*(N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    visit[a][b] = True
res = 4
newline(1, 0)
if res == 4:
    res = -1
print(res)


# def perm(n, arr):
#     if len(arr) == n:
#         print(arr)
#         return
#     for i in range(n):
#         if visit[i]:
#             continue
#         visit[i] = True
#         perm(n, arr+[i])
#         visit[i] = False
# def comb(arr, idx):
#     if len(arr) == n:
#         print(arr)
#         return
#     for i in range(idx+1, n):
#         comb(arr+[i], i)

# n = 3
# visit = [False]*n
# # perm(n, [])
# comb([], -1)


    