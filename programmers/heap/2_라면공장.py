def solution(stock, dates, supplies, k):
    if stock >= k:
        return 0
    dates.append(k-1)
    supplies.append(0)
    answer = 0
    day, st = (0, stock)
    # visit = [0]*len(dates)
    idx, s = 0, stock
    while idx < k:
        if s > dates[idx]:
            idx += 1
        elif s == dates[idx]:
            s += supplies[idx]
            idx += 1
            day, st = idx, s
            answer += 1
        else:
            idx = day
            st = s         

    return answer

# print(solution(4, [4, 10, 15], [20, 5, 10], 30))
print(solution(4, [1, 2, 3, 4], [10, 40, 20, 30], 100))
# print(solution(2, [4, 8], [9, 3], 30))