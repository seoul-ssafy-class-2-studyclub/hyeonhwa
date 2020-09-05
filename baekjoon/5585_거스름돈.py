import sys
input = lambda: sys.stdin.readline().rstrip()

n = 1000 - int(input())

res = 0
res += n//500
n = n%500
res += n//100
n = n%100
res += n//50
n = n%50
res += n//10
n = n%10
res += n//5
n = n%5
res += n
print(res)