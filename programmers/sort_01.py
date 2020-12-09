def changer(numbers):
    n = numbers
    for i in range((len(n) - 1), 0 , -1):
        for j in range(i):
            if int(str(n[j]) + str(n[j + 1])) < int(str(n[j + 1]) + str(n[j])):
                n[j], n[j + 1] = n[j + 1], n[j]
    n = [str(i) for i in n]
    return n

def solution(numbers):
    numbers = changer(numbers)
    answer = str(int(''.join(numbers)))
    return answer