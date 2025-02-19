import itertools

def solution(n,q,ans):
    candidates = list(itertools.combinations(range(1,n+1),5))
    m = len(ans)
    result = 0

    for password in candidates:
        index = 0
        while index < m:
            if ans[index] != len([i for i in password if i in q[index]]):
                break
            if index == m - 1:
                result += 1
            index += 1

    return result