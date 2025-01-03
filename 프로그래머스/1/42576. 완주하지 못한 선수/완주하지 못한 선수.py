def solution(participant, completion):
    player = {}
    index = 0
    for name in participant:
        player[hash(name)] = name
        index += hash(name)
    
    for name in completion:
        index -= hash(name)
    
    return player[index]