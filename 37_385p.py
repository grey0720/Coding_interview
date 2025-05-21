import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 거리는 0
for a in range(1, n + 1):
    graph[a][a] = 0

# 간선 정보 입력
for _ in range(m-1):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

# 플로이드-워셜 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        print(0 if graph[a][b] == INF else graph[a][b], end=' ')
    print()
