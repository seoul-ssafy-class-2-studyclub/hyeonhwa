def divide(arr):
    global stack
    l = len(arr)
    if l == 1:
        stack += arr
    elif l == 2:
        cp = compare(arr[0], arr[1])
        stack += [cp]
    else:
        if l % 2:
            return [divide(arr[0:l//2+1]), divide(arr[l//2+1:l])]
        else:
            return [divide(arr[0:l//2]), divide(arr[l//2:l])]


def compare(a, b):
    if a[1] > b[1]:
        if a[1] == 3 and b[1] == 1:
            return b
        else:
            return a
    elif a[1] < b[1]:
        if a[1] == 1 and b[1] == 3:
            return a
        else:
            return b
    else:
        if a[0] > b[0]:
            return b
        else:
            return a

# a = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 2]
# print(divide(a))

T = int(input())
for t in range(T):
    N = int(input())
    stack = []
    cards = []
    card = [int(i) for i in input().split()]
    for i in range(len(card)):
        cards.append([i, card[i]])
    while True:
        stack = []
        divide(cards)
        cards = stack
        if len(stack) == 1:
            break        

    print('#{} {}'.format(t+1, stack[0][0]+1))
