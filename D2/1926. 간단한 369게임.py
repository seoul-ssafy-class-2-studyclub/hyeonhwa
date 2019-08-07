N = int(input())
numbers = [i for i in range(1, N+1)]
numbers = list(map(str, numbers))
for i in numbers:
    if '3' in i or '6' in i or '9' in i:
        numbers[numbers.index(i)] = i.replace('3', '-').replace('6', '-').replace('9', '-')
for i in numbers:
    if '-' in i:
        numbers[numbers.index(i)] = '-' * i.count('-')
        
print(' '.join(numbers))