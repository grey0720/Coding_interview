import sys
input = sys.stdin.readline
n, m = map(int, input().split())
answer = 0
while n>1:
    if n%m ==0:
        n = n//m
    else:
        n = n-1
    answer += 1
print(answer)