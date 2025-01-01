def solution(phone_book):
    # 앞자리 숫자를 기준으로 정렬(오름차순 아님)
    phone_book.sort()

    # 반복문을 수행하면서 현재 번호와 다음 번호만 접두사 비교를 해줌
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False

    return True