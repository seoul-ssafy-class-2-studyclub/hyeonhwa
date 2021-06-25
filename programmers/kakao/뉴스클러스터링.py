def solution(str1, str2):
    l1, l2 = [], []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            l1.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            l2.append(str2[i:i+2].lower())
    union = []
    intersection = []
    for x in l1:
        if x in l2 and intersection.count(x) < min(l1.count(x), l2.count(x)):
            intersection.append(x)
    for x in l1:
        if union.count(x) < max(l1.count(x), l2.count(x)):
            union.append(x)
    for x in l2:
        if union.count(x) < max(l1.count(x), l2.count(x)):
            union.append(x)
    if not union or not intersection:
        return 65536
    return int((len(intersection)/len(union))*65536)

solution("FRANCE", "french")