def move():
    fst = {}
    for i in range(len(fire_balls)):
        r, c, m, s, d = fire_balls[i]
        dx, dy = idx[d]
        r, c = r+s*dx, c+s*dy
        if r < 1:
            while r < 1:
                r += n
        elif r > n:
            while r > n:
                r -= n
        if c < 1:
            while c < 1:
                c += n
        elif c > n:
            while c > n:
                c -= n
        if fst.get((r, c)):
            fst[(r, c)].append([m, s, d])
        else:
            fst[(r, c)] = [[m, s, d]]
    fire = []
    for key, value in fst.items():
        if len(value) > 1:
            ball_m, ball_s = 0, 0
            flag1, flag2 = 0, 0
            for i in range(len(value)):
                m, s, d = value[i]
                ball_m += m
                ball_s += s
                if d%2:
                    flag2 = 1
                else:
                    flag1 = 1
            ball_m //= 5
            fst[key] = []
            if ball_m > 0:
                ball_s //= len(value)
                if flag1 and flag2:
                    for j in range(1, 8, 2):
                        fst[key].append([ball_m, ball_s, j])
                else:
                    for j in range(0, 8, 2):
                        fst[key].append([ball_m, ball_s, j])
        for v in fst[key]:
            fire.append([key[0], key[1], v[0], v[1], v[2]])
    return fire


n, m, k = map(int, input().split())
fire_balls = [list(map(int, input().split())) for _ in range(m)]
cnt = 0
idx = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
while cnt < k:
    fire_balls = move()
    cnt += 1
res = 0
for ball in fire_balls:
    res += ball[2]
print(res)
