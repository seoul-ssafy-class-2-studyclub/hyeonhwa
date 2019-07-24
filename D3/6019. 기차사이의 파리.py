T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    b = input().split(' ')
    c = []  # int로 바꾼 b를 받을 리스트
    for i in b:
        i = int(i)
        c += [i]  # 받은 4개의 값을 변환해 저장한다, [D, A, B, F]
    time = c[0]/(c[1] + c[2])
    length = time * c[3]
    print(f'#{test_case}', length)