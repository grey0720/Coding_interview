import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int, input().split())

## 최단거리 테이블
graph = [[INF] for _ in range(n+1)]

# 자기 자신으로 가는 경우 0으로 초기화화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 간선 정보 입력
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 각 노드별로 거쳐가는 최단경로 구하기
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("Infinity")
        else:
            print(graph[a][b])