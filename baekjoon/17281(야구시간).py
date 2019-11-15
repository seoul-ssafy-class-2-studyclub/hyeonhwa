def getplayer(n):
    if n == 10:
        startgame(player)
        return
    for i in range(1, 10):
        if player[i] == 0:
            player[i] = n
            getplayer(n+1)
            player[i] = 0


def startgame(arr):
    global res
    score = 0
    start = 1
    for i in range(N):
        outscore = 0
        nxt = False
        base = [0]*3
        while True:
            for j in range(start, 10):
                if nums[i][arr[j]-1] == 0:
                    outscore += 1
                elif nums[i][arr[j]-1] == 1:
                    for m in range(2, -1, -1):
                        if base[m] == 1:
                            if m + 1 >= 3:
                                score += 1
                                base[m] = 0
                            else:
                                base[m+1] = 1
                                base[m] = 0
                    base[0] = 1
                elif nums[i][arr[j]-1] == 2:
                    for m in range(2, -1, -1):
                        if base[m] == 1:
                            if m + 2 >= 3:
                                score += 1
                                base[m] = 0
                            else:
                                base[m+2] = 1
                                base[m] = 0
                    base[1] = 1
                elif nums[i][arr[j]-1] == 3:
                    for m in range(3):
                        if base[m] == 1:
                            score += 1
                            base[m] = 0
                    base[2] = 1
                elif nums[i][arr[j]-1] == 4:
                    score += 1
                    for m in range(2, -1, -1):
                        if base[m] == 1:
                            score += 1
                            base[m] = 0
                if outscore == 3:
                    nxt = True
                    if j == 9:
                        start = 1
                    else:
                        start = j + 1
                    break
            if nxt == True:
                break
            start = 1
    res = max(res, score)


N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
player = [0]*10
player[4] = 1
res = 0
getplayer(2)
print(res)
