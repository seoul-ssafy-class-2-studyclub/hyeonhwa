T = int(input())

for t in range(1, T+1):
    N = int(input())
    if 1 <= N <= 10:
        array = [[0 for i in range(N)] for i in range(N)] # N*N 크기의 배열을 만든다
        value = 1
        row = N
        basic = 0
        while row > 0: # 열이 존재하는 동안 for문을 통해 숫자를 넣어준다
            for i in range(basic, basic+row):
                array[basic][i] = value
                value += 1
            for i in range(basic+1, basic+row):
                array[i][basic+row-1] = value
                value += 1
            for i in range(basic+row-2, basic-1, -1):
                array[basic+row-1][i] = value
                value += 1
            for i in range(basic+row-2, basic, -1):
                array[i][basic] = value
                value += 1
            basic += 1
            row -= 2
        print(f'#{t}')
        for i in array:
            print(' '.join(str(j) for j in i))
