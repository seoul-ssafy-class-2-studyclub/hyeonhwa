def solution(priorities, location):
    s = []
    i = 0
    priorities = list(enumerate(priorities))
    while priorities:
        if priorities[i][1] < max(priorities, key=lambda x:x[1])[1]:
            priorities.append(priorities.pop(0))
        else:
            s.append(priorities.pop(0))
    for i in range(len(s)):
        if s[i][0] == location:
            return i+1

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))