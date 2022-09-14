import collections


def solution(n, t, m, timetable):
    timetable.sort()
    tqueue = collections.deque(timetable)
    tdict = collections.defaultdict(list)
    for i in range(n):
        ph = (540 + i * t) // 60
        pm = (540 + i * t) % 60
        pivot = ("0" + str(ph) if ph < 10 else str(ph)) + ':' + ("0" + str(pm) if pm < 10 else str(pm))
        tdict[pivot] = list()
        while tqueue and tqueue[0] <= pivot and len(tdict[pivot]) < m:
            tdict[pivot].append(tqueue.popleft())
    maxtime = max(tdict.keys())
    if len(tdict[maxtime]) == 0:
        answer = maxtime
    else:
        temp = tdict[maxtime][-1]
        if len(tdict[maxtime]) == m:
            minustime = int(temp.split(':')[0]) * 60 + int(temp.split(':')[1]) - 1
            minush = minustime // 60
            minusm = minustime % 60
            answer = ("0" + str(minush) if minush < 10 else str(minush)) + ':' + (
                "0" + str(minusm) if minusm < 10 else str(minusm))
        else:
            answer = max(temp, maxtime)
    return answer