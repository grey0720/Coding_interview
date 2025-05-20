import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

# 간선 정보 저장할 2차원 변수 생성
graph = [[] for _ in range(n+1)]
# 최단거리 테이블
distance = [INF] * (n+1)

# graph에 간선정보 저장
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dstra(start):
    q = [] # heapq를 위한 q 선언
    heapq.heappush(q, (0, start)) # 0부터 start 까지 저장
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) # 최단거리 노드 pop
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1] # start노드에서 해당 노드까지 가는데 필요한 코스트
            if cost < distance[i[0]]: # 현재 코스트가 이전의 distance 보다 작으면 (최단값이 갱신 되었으면)
                distance[i[0]] = cost # 최단경로 테이블ㄴ 업데이트
                heapq.heappush(cost, i[0]) # 지금 start node에서 i[0]노드로 가는데 요구되는 코스트
dstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("Infinity")
    else:
        print(distance[i])