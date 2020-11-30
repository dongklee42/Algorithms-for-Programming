def solution(clothes):
    answer = 1
    c_dic = {}
    for item in clothes:
        if item[1] in c_dic:
            c_dic[item[1]].append(item[0])
        else:
            c_dic[item[1]] = [item[0]]
    for key in c_dic.keys():
        answer *= (len(c_dic[key]) + 1)
    return answer - 1
