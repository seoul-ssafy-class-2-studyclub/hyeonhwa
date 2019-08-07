T = int(input())
for t in range(T):
    clock = list(map(int, input().split()))
    cnt = 0
    mins = clock[1] + clock[3]
    if mins >= 60:
        cnt = mins//60
        mins = mins%60
    hours = clock[0] + clock[2] + cnt
    if hours > 12:
        hours -= 12
    print(f'#{t+1} {hours} {mins}')