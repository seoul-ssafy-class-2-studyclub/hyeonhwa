def solution(budgets, M):
    if sum(budgets) <= M:
        return max(budgets)

    def limitsum(budgets, limit):
        total = 0
        for budget in budgets:
            if budget > limit:
                budget = limit
            total += budget
        return total

    low = 0
    high = max(budgets)
    res = 0
    total_budget = 0

    while low < high:
        mid = (low+high) // 2
        total = limitsum(budgets, mid)
        if total == M:
            return mid
        elif total < M:
            low = mid + 1
            if total_budget < total:
                total_budget = total
                res = mid
        else:
            high = mid
    return res

solution([120, 110, 140, 150], 485)