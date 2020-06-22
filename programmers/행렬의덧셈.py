def solution(arr1, arr2):
    ans = []
    for i in range(len(arr1)):
        arr = []
        for j in range(len(arr1[i])):
            arr.append(arr1[i][j] + arr2[i][j])
        ans.append(arr)
    return ans