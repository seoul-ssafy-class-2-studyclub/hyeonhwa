def solution(numbers):
    numbers = list(map(str, numbers))
    # 문자열 정렬 : 첫 글자가 큰 순서, 문자열의 길이가 긴 순서
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))
