def solution(n, m, section):
    count = 1
    index = 1
    while len(section) > index:
        if section[index] >= section[index-1]+m:
            count += 1
            index += 1
        else:
            section.pop(index)
    return count 