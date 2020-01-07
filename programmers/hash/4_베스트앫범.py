def solution(genres, plays):
    answer = []
    musics = {}
    total = {}
    for i in range(len(genres)):
        if not musics.get(genres[i]):
            musics[genres[i]] = [(i, plays[i])]
            total[genres[i]] = plays[i]
        else:
            musics[genres[i]].append((i, plays[i]))
            total[genres[i]] += plays[i]
    maxgenres = []
    for values in total.values():
        maxgenres.append(values)
    maxgenres.sort(reverse=True)
    for genre in range(len(maxgenres)):
        for key in total.keys():
            if total[key] == maxgenres[genre]:
                maxgenres[genre] = key
    for genre in maxgenres:
        musics[genre].sort(key=lambda x:x[1], reverse = True)
        if len(musics[genre]) > 1:
            answer.append(musics[genre][0][0])
            answer.append(musics[genre][1][0])
        else:
            answer.append(musics[genre][0][0])
    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))