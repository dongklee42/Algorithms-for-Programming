def solution(phone_book):
    for i in range(len(phone_book)):
        j = i + 1
        while j < len(phone_book):
            if phone_book[j].find(phone_book[i]) == 0 or phone_book[i].find(phone_book[j]) == 0:
                return False
            j += 1
    return True
