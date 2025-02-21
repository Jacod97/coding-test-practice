def solution(schedules, timelogs, startday):
    safetime = []
    for arrive in schedules:
        arrive += 10
        if arrive % 100 >= 60:
            arrive += 40
        if arrive >= 2400:
            arrive -= 2400
        safetime.append(arrive)
    # print(safetime)
    count = len(safetime)
        
    for i in range(len(schedules)):
        today = startday # 오늘의 요일 초기화
        for time in timelogs[i]:
            if today == 6 or today == 7:
                today += 1
                continue
            elif today > 7:
                today -= 7
                
            if time > safetime[i]:
                count -= 1
                break
            else:
                today += 1
    return count
            