def divd(st):
    x_point = 1
    y_point = 0
    
    for i in range(1,len(st)):
        if st[0] == st[i]:
            x_point += 1
        else:
            y_point += 1
        if x_point == y_point:
            break
    return [st[:x_point*2], st[x_point*2:]]

def solution(s):
    answer = []
    length = 0
    st = s
    
    while len(s) != length:
        answer.append(divd(st)[0])
        length += len(divd(st)[0])
        st = divd(st)[1]
        
    return len(answer)