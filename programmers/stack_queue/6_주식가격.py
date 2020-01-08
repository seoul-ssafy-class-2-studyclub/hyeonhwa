def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)):
        res = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                res += 1
            else:
                res += 1
                break
        answer[i] = res
    return answer

print(solution([1, 2, 3, 2, 3]))