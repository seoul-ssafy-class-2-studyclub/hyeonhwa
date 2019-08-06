T = int(input())
for t in range(T):
    S = input()
    n = []
    cards = {'S': [], 'D': [], 'H': [], 'C': []}
    for i in range(0,len(S),3):
        n.append(S[i:i+3])
    for i in n:
        for key in cards.keys():
            if i[0] == key:
                if int(i[1:3]) not in cards[key]:
                    cards[key] += [int(i[1:3])]
                else:
                    result = 'ERROR'
                    break
    if result:
        print('#{} {}'.format(t+1, result))
    else:
        print('#{} {} {} {} {}'.format(t+1, 13 - len(cards['S']), 13 - len(cards['D']), 13 - len(cards['H']), 13 - len(cards['C'])))
