n, k = map(int, input().split())
conveyor = list(map(int, input().split()))
robot = [0]*2*n
cnt = 0
res = 0
while cnt < k:
    re_c = [0]*2*n
    re_b = [0]*2*n
    for i in range(2*n-1):
        re_c[i+1] = conveyor[i]
        if i+1 == n and robot[i]:
            robot[i] = 0
        re_b[i+1] = robot[i]
    re_c[0] = conveyor[2*n-1]
    re_b[0] = robot[2*n-1]
    conveyor = re_c
    robot = re_b
    for i in range(n-1, -1, -1):
        if i == n-1 and robot[i]:
            robot[i] = 0
        elif robot[i]:
            if not robot[i+1] and conveyor[i+1] > 0:
                robot[i+1] = 1
                robot[i] = 0
                conveyor[i+1] -= 1
    if not robot[0] and conveyor[0] > 0:
        robot[0] = 1
        conveyor[0] -= 1
    res += 1
    if conveyor.count(0) >= k:
        break
print(res)
