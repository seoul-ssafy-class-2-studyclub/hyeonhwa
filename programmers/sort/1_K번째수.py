def solution(array, commands):
    ans = []
    for command in commands:
        arr = array[command[0]-1:command[1]]
        arr.sort()
        ans.append(arr[command[2]-1])
    return ans