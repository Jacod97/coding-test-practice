def solution(video_len, pos, op_start, op_end, commands):
    function = [video_len, pos, op_start, op_end]
    second = [(int(i[:2]) * 60) + int(i[-2:]) for i in function]
    
    # commands 작동 전 pos
    if second[2] <= second[1] < second[3]:
        second[1] = second[3]
    # commands 작동
    for i in range(len(commands)):
        if commands[i] == 'next':
            second[1] += 10
        elif commands[i] == 'prev':
            second[1] -= 10
    # pos 경계    
        if second[1] < 0:
            second[1] = 0
        if second[1] > second[0]:
            second[1] = second[0]
        if second[2] <= second[1] < second[3]:
            second[1] = second[3]
            
    # second -> "분:초"로 바꾸기
    m = f"{second[1] // 60}"
    if 0 < second[1] // 60 < 10:
        m = "0"+m
    elif second[1] // 60 == 0:
        m = "00"
    
    s = f"{second[1] % 60}"
    if 0 < second[1] % 60 < 10:
        s = "0"+s
    elif second[1] % 60 == 0:
        s = "00"
        
    return m+':'+s