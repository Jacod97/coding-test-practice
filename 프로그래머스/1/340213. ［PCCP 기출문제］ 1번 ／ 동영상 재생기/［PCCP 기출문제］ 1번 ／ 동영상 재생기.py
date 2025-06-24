def convert_time(time):
    if type(time) == str:
        conv_time = int(time[:2])*60 + int(time[3:])
    else:
        if time // 60 < 10:
            head = f"0{time//60}"
        else:
            head = str(time//60)
        if time % 60 < 10:
            tail = f"0{time%60}"
        else:
            tail = str(time%60)
        conv_time = f"{head}:{tail}"
    return conv_time

def solution(video_len, pos, op_start, op_end, commands):
    i_pos = convert_time(pos)
    i_start = convert_time(op_start)
    i_end = convert_time(op_end)
    i_len = convert_time(video_len)
    if i_pos >= i_start and i_pos <= i_end:
        i_pos = i_end
    for c in commands:
        if c == "next":
            i_pos += 10
            if i_pos > i_len:
                i_pos = i_len
        elif c == "prev":
            i_pos -= 10
            if i_pos < 0:
                i_pos = 0
        if i_pos >= i_start and i_pos <= i_end:
            i_pos = i_end

    return convert_time(i_pos)
    
# 10초 전 이동
# 10초 후 이동
# 오프닝 건너뛰기