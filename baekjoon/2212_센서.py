import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
k = int(input())
sensors = [int(i) for i in input().split()]
sensors.sort()
diff = []
for i in range(1, len(sensors)):
    diff.append(sensors[i]-sensors[i-1])
diff.sort()
x = len(diff) - k + 1
print(sum(diff[:x]))