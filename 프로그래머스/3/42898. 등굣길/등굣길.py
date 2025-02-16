def solution(m, n, puddles):
    mymap = [[0] * m for i in range(n)]
    mymap[0][0] = 1
    for y in range(n):
        for x in range(m):
            
            if [x+1, y+1] in puddles:
                mymap[y][x] = 0
                # print(f"첫번째 웅덩이 mymap : {mymap}")
                continue

            if x < 1 and y > 0:
                mymap[y][x] = mymap[y-1][x]

            elif x > 0 and y < 1:
                mymap[y][x] = mymap[y][x-1]

            else:
                if [x,y] == [0,0]:
                    continue
                else:
                    mymap[y][x] = mymap[y-1][x] + mymap[y][x-1]

            # print(f"y : {y}, x : {x}  {mymap}")
    return mymap[n-1][m-1] % 1000000007