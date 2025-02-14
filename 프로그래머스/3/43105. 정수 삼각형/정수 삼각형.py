def solution(triangle):
    lenth = len(triangle)
    a = [[0]*i for i in range(1,lenth+1)]
    a[0][0] = triangle[0][0]

    for n in range(1,lenth):
        for m in range(len(triangle[n])):
            # a[n][m] = max(a[n-1][m-1], a[n-1][m]) + triangle[n][m]
            if m == 0:
                a[n][m] = a[n-1][m] + triangle[n][m]
            elif m == len(triangle[n])-1:
                a[n][m] = a[n-1][m-1] + triangle[n][m]
            else:
                a[n][m] = max(a[n-1][m-1], a[n-1][m]) + triangle[n][m]
    
    return max(a[lenth - 1])

