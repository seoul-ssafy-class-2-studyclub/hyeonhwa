def solution(stock, dates, supplies, k):
    if stock >= k:
        return 0
    answer = 0
    i = -1
    while i < len(dates)-1:
        day = stock
        for j in range(len(dates)-1, i, -1):
            if day >= k:
                return answer
            if day >= dates[j]:
                i = j
                stock += supplies[i]
                answer += 1
                break
            elif day < dates[j]:
                if j - 1 != i:
                    continue
                return
    return answer

print(solution(4, [4, 10, 15], [20, 5, 10], 30))