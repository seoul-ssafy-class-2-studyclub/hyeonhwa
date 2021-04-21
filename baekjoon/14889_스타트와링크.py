# combination
# from itertools import combinations
# combinations(s, n//2)

def comb(arr, idx):
    if len(arr) == n//2:
        comb_l.append(arr)
        return
    for i in range(idx+1, n):
        comb(arr+[i], i)


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
comb_l = []
comb([], -1)
res = 1e10
for i in range(len(comb_l)//2):
    start, link = 0, 0
    start_team = comb_l[i]
    link_team = comb_l[-i-1]
    for i in range(n//2):
        for j in range(n//2):
            start += s[start_team[i]][start_team[j]]
            link += s[link_team[i]][link_team[j]]
    res = min(res, abs(start-link))
print(res)
