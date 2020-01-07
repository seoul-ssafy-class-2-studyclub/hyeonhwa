def solution(heights):
    answer = [0]*len(heights)
    for i in range(len(heights)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                answer[i] = j + 1
                break
    return answer

print(solution([6, 9, 5, 7, 4]))
print(solution([3, 9, 9, 3, 5, 7, 2]))
print(solution([1, 5, 3, 6, 7, 6, 5]))