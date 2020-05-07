import datetime

def solution(lines):
    times = []
    alltime = []
    for line in lines:
        line = list(line.split())
        finish = list(line[1].split(':'))
        msec = list(finish[2].split('.'))
        finish = datetime.datetime(2016, 9, 15, int(finish[0]), int(finish[1]), int(msec[0]), int(msec[1])*1000)
        deal = float(line[2][:-1])
        start = finish - datetime.timedelta(seconds=round(deal - 0.001, 3))
        time = [start, finish]
        times.append(time)
        alltime.extend(time)
    alltime.sort()
    answer = 0
    i = 0
    while i < len(alltime):
        ans = 0
        s = alltime[i]
        re_s = s + datetime.timedelta(seconds=0.999)
        for time in times:
            if s <= time[0] <= re_s or s <= time[1] <= re_s or time[0] <= s <= time[1] or time[0] <= re_s <= time[1]:
                ans += 1
        answer = max(ans, answer)
        i += 1
    return answer


solution([
'2016-09-15 01:00:04.002 2.0s',
'2016-09-15 01:00:07.000 2s'
])