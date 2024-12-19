import datetime

def solution(a, b):
    # 2016년 a월 b일 날짜 생성
    date = datetime.date(2016, a, b)
    # 요일 계산 (0: 월요일, 1: 화요일, ..., 6: 일요일)
    weekdays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return weekdays[date.weekday()]