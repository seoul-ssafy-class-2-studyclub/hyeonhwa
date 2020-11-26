def solution(citations):
    citations.sort(reverse=True)
    h = 0
    if citations[-1] > len(citations):
        return len(citations)
    for i in range(len(citations)):
        if i+1 >= citations[i]:
            if i+1 == citations[i]:
                h = i+1
            else:
                h = i
            break
    return h

print(solution([10, 11, 12, 13]))