T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-']
for i in range(1, T+1):
    N, K = input().split(' ')
    if int(N) % 10 == 0 and 10 <= int(N) <= 100 and 1 <= int(K) <= int(N):
        total = []
        total_n = []
        for n in range(1, int(N)+1):
            score = input().split(' ')
            total.append(0.35*int(score[0])+0.45*int(score[1])+0.2*int(score[2]))
        k = total[int(K)-1]
        if total.count(k) > 1:
            break
        total = list(sorted(total, reverse=True))
        for t in range(0, len(total), int(N)//10):
            total_n.append(total[t:t+(int(N)//10)])
        result = dict(zip(grade, total_n))
        for key,value in result.items():
            if k in value:
                print(key)