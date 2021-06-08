def solution(new_id):
    answer = ''
    for id in new_id:
        if not answer and id == '.':
            continue
        elif id.isupper():
            answer += id.lower()
        elif id.islower() or id.isdigit() or id == '-' or id == '_':
            answer += id
        elif id == '.' and answer and answer[-1] != '.':
            answer += id
    if len(answer) > 15:
        answer = answer[:15]
    if answer and answer[-1] == '.':
        answer = answer[:len(answer)-1]
    if len(answer) == 0:
        answer = 'aaa'
    if len(answer) <= 2:
        while len(answer) <= 2:
            answer += answer[-1]
    return answer
