def solution(phone_book):
    phone = {}
    # 사전순으로 정렬 후 폰번호와 길이를 딕셔너리에 저장
    # (해시 문제라서 굳이 딕셔너리에 넣었지만 "굳이"인것 같다..)
    phone_book.sort()
    for number in phone_book:
        phone[number] = len(number)
    # 머가리 길이 추출
    head = list(phone.values())
    # 머가리 길이만큼 문자열 슬라이싱 해주는데 같으면 false
    for i in range(len(head)-1):
        if phone_book[i] == phone_book[i+1][:head[i]]:
            return False
            break
    return True