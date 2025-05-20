'''
전형적인 floyd-warshall 문제
2차원 리스트로 a부터 b까지 가는 최단 경로를 관리해야 함
단, 각 노드의 가중치는 "1"로 고정
'''
import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int, input().split())

# 최단경로 테이블
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 노드는 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐가는 노드 x, 최종으로 도착하는 노드 k
x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

## start node = 1, 거쳐가는 노드 x, 최종 노드 k
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)

