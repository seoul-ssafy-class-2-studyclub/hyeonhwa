def solution(lottos, win_nums):
    order = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    answer = []
    cnt = 0
    for num in win_nums:
        if num in lottos:
            cnt += 1
    zero = lottos.count(0)
    answer.append(order[cnt+zero])
    answer.append(order[cnt])
    return answer