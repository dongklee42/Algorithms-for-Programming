# k번째 수
def bb_sort(data):
    for i in range((len(data) - 1), 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def solution(array, commands):
    answer = []
    for com in commands:
        temp = array[(com[0] - 1) : com[1]]
        bb_sort(temp)
        answer.append(temp[com[2] - 1])
        print(answer)
    return answer
