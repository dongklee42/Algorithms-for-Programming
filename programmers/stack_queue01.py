# 기능개발
from math import ceil

def solution(progresses, speeds):
    answer = []
    days = 1
    for i, p in enumerate(progresses):
        progresses[i] = ceil((100 - p) / speeds[i])
    for i in range(1, len(progresses)):
        if progresses[i - 1] >= progresses[i]:
            days += 1
            continue
        else:
            answer.append(days)
            days = 1
    answer.append(days)
    return answer