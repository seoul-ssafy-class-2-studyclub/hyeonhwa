T = int(input())

for t in range(1, T+1):
    N, M = input().split(' ')
    mul = []  # 각각의 결과를 저장할 리스트 생성
    if 3 <= int(N) and int(M) <= 20:
        aj = [int(i) for i in input().split(' ')]
        bj = [int(i) for i in input().split(' ')]
        if len(aj) == int(N) and len(bj) == int(M):
            if int(N) > int(M):  # 처음으로 넣은 리스트가 더 길 경우 순서를 바꿔준다
                aj, bj = bj, aj
            j = 0
            for j in range(len(bj)-len(aj)+1):  # 짧은 리스트의 마지막이 긴 리스트의 마지막으로 올 때까지 돌려준다.
                add = 0
                for i in range(len(aj)):  # 각 자리를 곱해서 더해준다.
                    add += aj[i]*bj[i]
                aj.insert(0, 0)
                mul.append(add)
    print(f'#{t} {max(mul)}')  # 리스트에서 최댓값을 구해서 출력