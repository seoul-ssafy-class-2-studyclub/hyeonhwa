N = int(input())
switch = list(map(int, input().split()))
n = int(input())
students = []
for i in range(n):
    students += [list(map(int, input().split()))]
for i in range(len(students)):
    s = students[i][1]
    if students[i][0] == 1:
        j = 1
        while j * s - 1 < N:
            if j * s - 1 >= N:
                break
            if switch[j * s - 1]: 
                switch[j * s - 1] = 0
            else:
                switch[j * s - 1] = 1
            j += 1
    elif students[i][0] == 2:
        k = 1
        if switch[s-1]:
            switch[s-1] = 0
        else:
            switch[s-1] = 1
        while s - k > 0 and s + k < N + 1 and switch[s-k-1] == switch[s+k-1]:
            if switch[s-k-1] == 1:
                switch[s-k-1] = 0
                switch[s+k-1] = 0
            else:
                switch[s-k-1] = 1
                switch[s+k-1] = 1
            k += 1
for i in range(0, len(switch), 20):
    l = ' '.join(list(map(str, switch[i:i+20])))
    print(l)
