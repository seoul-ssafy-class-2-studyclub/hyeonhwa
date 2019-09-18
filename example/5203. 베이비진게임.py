T = int(input())
for t in range(T):
    cards = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    flag = 0
    for i in range(0, 12, 2):
        p1[cards[i]] += 1
        if i >= 6:
            if flag == 0:
                if p1[cards[i]] == 3:
                    flag = 1
                    break
            if flag == 0:
                for j in range(8):
                    if p1[j] and p1[j+1] and p1[j+2]:
                        flag = 1
                        break
        if flag:
            break
        p2[cards[i+1]] += 1
        if i >= 6:
            if flag == 0:
                if p2[cards[i+1]] == 3:
                    flag = 2
                    break
            if flag == 0:
                for j in range(8):
                    if p2[j] and p2[j+1] and p2[j+2]:
                        flag = 2
                        break
        if flag:
            break
    print('#{} {}'.format(t+1, flag))
