def solution(record):
    result = []
    uid = {}
    for x in record:
        x = list(x.split())
        if x[0] == 'Enter':
            uid[x[1]] = x[2]
            result.append([x[1], "님이 들어왔습니다."])
        elif x[0] == 'Leave':
            result.append([x[1], "님이 나갔습니다."])
        else:
            uid[x[1]] = x[2]
    for i in range(len(result)):
        x = result[i]
        x[0] = uid[x[0]]
        result[i] = x[0]+x[1]
    return result
    

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
