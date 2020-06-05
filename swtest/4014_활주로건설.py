def check(i, m, k):
    if k == 0:
        for j in range(m):
            if i + j < n:
                if visit[i+j] == 1 or arr[i+j] != arr[i]:
                    return False
            else:
                return False
        return True
    else:
        for j in range(1, m+1):
            if i - j >= 0:
                if visit[i-j] == 1 or arr[i-j] != num:
                    return False
            else:
                return False
        return True

for t in range(int(input())):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for x in range(n):
        arr = board[x]
        visit = [0]*n
        num = arr[0]
        flag = 0
        for i in range(1, n):
            if num == arr[i]:
                continue
            if abs(num-arr[i]) > 1:
                flag = 1
                break
            if abs(num-arr[i]) == 1:
                if num > arr[i]:
                    if check(i, m, 0):
                        for j in range(m):
                            visit[i+j] = 1
                    else:
                        flag = 1
                        break
                else:
                    if check(i, m, 1):
                        for j in range(1, m+1):
                            visit[i-j] = 1
                    else:
                        flag = 1
                        break
                num = arr[i]
            else:
                flag = 1
                break
        if flag == 0:
            res += 1

    for x in range(n):
        arr = []
        for y in range(n):
            arr.append(board[y][x])
        visit = [0]*n
        num = arr[0]
        flag = 0
        for i in range(1, n):
            if num == arr[i]:
                continue
            if abs(num-arr[i]) > 1:
                flag = 1
                break
            if abs(num-arr[i]) == 1:
                if num > arr[i]:
                    if check(i, m, 0):
                        for j in range(m):
                            visit[i+j] = 1
                    else:
                        flag = 1
                        break
                else:
                    if check(i, m, 1):
                        for j in range(1, m+1):
                            visit[i-j] = 1
                    else:
                        flag = 1
                        break
                num = arr[i]
            else:
                flag = 1
                break
        if flag == 0:
            res += 1
    print(f'#{t+1} {res}')

