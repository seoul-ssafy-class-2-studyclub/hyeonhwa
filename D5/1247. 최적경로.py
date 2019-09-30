def move(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def back(s, arr=[0]):
    global res
    if s < res:
        rearr = arr[:]
        for i in range(N+1):
            if i not in rearr:
                rearr = arr+[i]
                temp = s+move(re_location[rearr[-2]][0], re_location[rearr[-2]][1], re_location[rearr[-1]][0], re_location[rearr[-1]][1])
                if temp < res:
                    back(temp, rearr)
                    if len(rearr) == N+1 and temp + move(re_location[rearr[-1]][0], re_location[rearr[-1]][1], locations[1][0], locations[1][1]) < res:
                        res = temp+move(re_location[rearr[-1]][0], re_location[rearr[-1]][1], locations[1][0], locations[1][1])


T = int(input())
for t in range(T):
    N = int(input())
    board = list(map(int, input().split()))
    locations = []
    for i in range(0, len(board), 2):
        locations.append((board[i], board[i+1]))
    res = 1000000
    re_location = [locations[i] for i in range(len(locations)) if i != 1]
    back(0)
    print('#{} {}'.format(t+1, res))