T = int(input())
for t in range(T):
    score = list(map(int, input().split()))
    for i in range(len(score)):
        if score[i] < 40:
            score[i] = 40

    average = int(sum(score)/5)

    print(f'#{t+1} {average}')