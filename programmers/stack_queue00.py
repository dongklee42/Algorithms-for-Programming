# 주식가격 : 시간초과 문제 있었음

def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range((i + 1), len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)
    return answer