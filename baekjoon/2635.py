from time import time
start = time()

N = int(input())
length = 0

for i in range(N//2, N+1):
    numbers = [N, i]
    while numbers[-2] >= numbers[-1]:
        numbers += [numbers[-2]-numbers[-1]]
        if numbers[-2] < numbers[-1]:
            break
    if length <= len(numbers):
        length = len(numbers)
        result = numbers

print(length)
print(' '.join(list(map(str, result))))
print(time()-start)