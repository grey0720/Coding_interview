'''
그리디 알고리즘
무난히 패스
'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
card = []
mx = 0
answer = 0

for i in range(n):
    l = list(map(int, input().split()))
    if mx < min(l):
        answer = i
        mx = min(l)

print(mx)