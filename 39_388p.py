'''
python3 {파일명} < input.txt
출력예시랑 안맞는 경우가 존재함 -> 으르렁 지피티가 입력 예시 잘못 변환해줬어 으르렁렁
'''
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
test_case = int(input())
for i in range(test_case):
    print(f'test_case : {i}')

    n = int(input())
    graph = []
    distance = [[INF]*(n) for _ in range(n)]
    for _ in range(n):
        li = list(map(int, input().split()))
        graph.append(li)
    print("graph1", graph)
    dir = [[0,1],[0,-1],[1,0],[-1,0]]

    a,b = 0, 0
    q = []
    heapq.heappush(q, (graph[a][b], a, b))
    distance[a][b] = graph[a][b]

    while q:
        dist, x, y = heapq.heappop(q)
        if dist > distance[x][y]:
            continue

        for [dx, dy] in dir:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    
    print("last", distance[n-1][n-1])