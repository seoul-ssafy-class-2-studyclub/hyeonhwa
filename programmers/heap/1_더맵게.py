import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        if len(scoville) > 1:
            x = heapq.heappop(scoville)
            y = heapq.heappop(scoville)
            z = x + 2*y
            heapq.heappush(scoville, z)
        else:
            return -1
        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))