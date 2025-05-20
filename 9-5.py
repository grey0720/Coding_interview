'''
전보 문제
다익스트라 알고리즘
우선순위 큐, heapq 사용
'''
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
## 노드&간선 정보 저장
graph = [[] for i in range(n+1)]
## 최단거리
distance = [INF]*(n+1)

## 간선 정보 저장
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dstra(start):
    q = [] # 우선순위 큐 준비
    heapq.heappush(q, (0, start))
    distance[start] = 0 ## 제자리는 0으로 초기화
    while q:
        dist, now = heapq.heappop(q)

        ## 이미 방문한 노드는 무시
        if distance[now] < dist:
            continue
        # 현재 위치한 노드에 인접한 노드 정보 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (0, i[0]))

dstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
print(count-1, max_distance)