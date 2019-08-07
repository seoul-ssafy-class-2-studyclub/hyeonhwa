T = int(input())

for t in range(1, T+1):
    N = int(input())
    money = {50000 : 0, 10000 : 0, 5000 : 0, 1000 : 0, 500 : 0, 100 : 0, 50 : 0, 10 : 0,}
    for key in money.keys():
        if N // key:
            money[key] = N//key
            N -= (N//key)*key
    print(f'#{t}')
    for key, value in money.items():
        if key == 10:
            print(value)
        else:
            print(value, end=' ')