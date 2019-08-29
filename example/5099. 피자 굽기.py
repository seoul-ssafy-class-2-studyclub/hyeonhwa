def circle():
    queue = pizzas[0:N]
    n = N
    p = []
    result = []
    while queue:
        x = queue.pop(0)
        x[1] = x[1]//2
        if x[1] == 0:
            result.append(x)
            if n < M:
                p.append(pizzas[n])
                n += 1
        else:
            p.append(x)
        if not queue:
            queue = p
            p = []
    return result[-1]


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    idx = [i for i in range(M)]
    value = Ci[:]
    pizza = list(zip(idx, value))
    pizzas = []
    for x, y in pizza:
        pizzas.append([x, y])
    res = circle()
    print('#{} {}'.format(t+1, res[0]+1))