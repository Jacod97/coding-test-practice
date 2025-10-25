# Node, Edges, i for i in village if k >= i
import heapq

def solution(N, road, K):
    INP = 10000000
    temp = [INP] * N
    temp[0] = 0

    graph = [[] for _ in range(N)]
    for a,b,cost in road:
        a -= 1
        b -= 1
        graph[a].append((cost, b))
        graph[b].append((cost, a))

    dn = [(0,0)]
    while dn:

        d,n = heapq.heappop(dn)
        if d > temp[n]:
            continue

        for next_d, next_n in graph[n]:
            if temp[next_n] > d + next_d:
                temp[next_n] = d + next_d
                heapq.heappush(dn,(d+next_d, next_n))
    
    count = 0
    for val in temp:
        if val > K:
            continue
        count += 1
    return count
    
            
        