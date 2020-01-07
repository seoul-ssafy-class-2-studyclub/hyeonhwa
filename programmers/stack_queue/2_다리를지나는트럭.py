def solution(bridge_length, weight, truck_weights):
    answer = 0
    go = [[truck_weights[0], 0]]
    idx = 1
    while go:
        for i in go[:]:
            i[1] += 1
            if i[1] == bridge_length:
                go.remove(i)
        s = 0
        for i in go:
            s += i[0]
        if idx < len(truck_weights) and s + truck_weights[idx] <= weight:
            go.append([truck_weights[idx], 0])
            idx += 1
        answer += 1
    return answer + 1

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
