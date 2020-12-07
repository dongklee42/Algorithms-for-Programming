def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    answer = 0
    while answer < n:
        answer += 1
        if answer >= citations[answer - 1]:
            break
    return answer
