dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())
for t in range(T):
    date = list(map(int, input().split()))
    if date[0] == date[2]:
        dif = date[3] - date[1] + 1
    else:
        i = date[0]
        dif = dates[date[0]-1] - date[1] + 1
        while i < date[2]-1:
            dif += dates[i]
            i += 1
            if i == date[2]-1:
                break
        dif += date[3]
    print(f'#{t+1} {dif}')
