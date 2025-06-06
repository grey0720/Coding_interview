'''
greedy 알고리즘
사실 이게 왜 그리디인지 잘 모르겠음
'''
import sys
input = sys.stdin.readline

m,n,k = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
a = n//(k+1)
b = n %(k+1)

answer = a*(l[0]*k + l[1]) + b*(l[0])
print(answer)