T = int(input())
for t in range(T):
    str1 = input()
    str2 = input()
    numbers = []
    for i in str1:
        numbers += [str2.count(i)]
    print('#{} {}'.format(t+1, max(numbers)))