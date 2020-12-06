# 가장 큰 수(수정 필요)
def comb_digits(num_list):
    comb_list = []
    for i, n in enumerate(num_list):
        num = 0
        num += num_list[i]
        for j in range(len(num_list)):
            if i != j:
                num = (num * 10**(len(str(num_list[j])))) + num_list[j]
        comb_list.append(num)
    return comb_list


def solution(numbers):
    num_list = comb_digits(numbers)
    num_list.sort()
    print(num_list)
    answer = str(num_list[-1])
    return answer
