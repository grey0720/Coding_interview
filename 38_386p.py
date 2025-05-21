'''
이게 제일 어려웠다
플로이드 마샬을 이용해 "모든 노드에 도달 가능한가?"를 확인해야 함
답 보고 풀었다...으르렁
'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split()) # n = 학생 수, m = 비교 횟수
INF = int(1e9)

#최단거리 테이블
distance = [[INF] * (n+1) for _ in range(n+1)] ## 플로이드 워셜로
# 만약 해당 행에서 INF 있으면 순위 비교 불가로 

for a in range(1, n+1):
    distance[a][a] = 0

## 한번 비교할때마다 1 추가
for _ in range(m):
    a,b = map(int, input().split())
    distance[a][b] = 1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            distance[a][b] = min(distance[a][b], distance[a][k]+distance[k][b])

result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if distance[i][j] != INF or distance[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)