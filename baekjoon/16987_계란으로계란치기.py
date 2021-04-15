def sol(ans, idx):
    global res
    if idx == n:
        res = max(ans, res)
        return
    if eggs[idx][0] <= 0:
        sol(ans, idx+1)
    else:
        flag = 0
        for j in range(n):
            if idx != j and eggs[j][0] > 0:
                flag = 1
                eggs[j][0] -= eggs[idx][1]
                eggs[idx][0] -= eggs[j][1]
                if eggs[j][0] <= 0:
                    ans += 1
                if eggs[idx][0] <= 0:
                    ans += 1
                sol(ans, idx+1)
                if eggs[j][0] <= 0:
                    ans -= 1
                if eggs[idx][0] <= 0:
                    ans -= 1
                eggs[j][0] += eggs[idx][1]
                eggs[idx][0] += eggs[j][1]
        if not flag:
            res = max(ans, res)


n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
res = 0
sol(0, 0)
print(res)
