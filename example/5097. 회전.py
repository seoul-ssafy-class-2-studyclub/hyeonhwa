T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    for _ in range(M):
         num = numbers.pop(0)
         numbers.append(num)
    print('#{} {}'.format(t+1,numbers[0]))