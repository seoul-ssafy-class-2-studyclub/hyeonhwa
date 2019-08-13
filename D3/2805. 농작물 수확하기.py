T = int(input())
for t in range(T):
    N = int(input())
    value = [[i for i in input()] for j in range(N)]
    values = []
    for i in value:
        values += [list(map(int, i))]
    std = N//2 # standard
    k = 1
    newvalue = [values[std]]
    while std + k <= N and std - k >= 0:
        newvalue += [values[std-k][k:len(values)-k]]
        newvalue += [values[std+k][k:len(values)-k]]
        k += 1
    mysum = 0
    for i in newvalue:
        mysum += sum(i)
    print('#{} {}'.format(t+1, mysum))
