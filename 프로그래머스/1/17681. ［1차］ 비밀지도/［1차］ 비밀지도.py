import re

def create_map(n,arr):
    two_map = [bin(i) for i in arr]
    complet_map = []
    for i in range(n):
        complet_map.append([int(x) for x in two_map[i] if x != 'b'])
        if len(complet_map[i]) > n:
            del complet_map[i][0]
        elif len(complet_map[i]) < n:
            complet_map[i] = [0] * (n-len(complet_map[i])) + complet_map[i]
    return complet_map

def solution(n, arr1, arr2): 
    arr1 = create_map(n,arr1)
    arr2 = create_map(n,arr2)
    
    answer = [[str(c+d) for c,d in zip(a,b)] for a,b in zip(arr1,arr2)]
    for i in range(n):
        answer[i] = ''.join(answer[i])
        answer[i] = re.sub('[1-2]', '#', answer[i])
        answer[i] = re.sub('[0]', ' ', answer[i])
    return answer