T = int(input())

numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

for t in range(1, T+1):
    N = input().split('\n')
    for n in N:
        n = int(n)
        k = 1
        result = []
        while True:
            for i in str(k * n):
                result.append(int(i))
            k += 1
            if set(result) == numbers:
                print(f'#{t} {(k-1) * n}')
                break