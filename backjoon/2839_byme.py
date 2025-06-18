'''
dp 문제
한번에 통과 드디어
'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)

for i in range(n+1):
    ## 초기 설정
    if i == 1 or i == 2 or i ==4:
        dp[i] = -1
    if i == 3 or i == 5:
        dp[i] = 1
    if i > 3 and dp[i-5] == -1 and dp[i-3] == -1:
        dp[i] = -1
    if i > 5 and dp[i-5] > 0:
        dp[i] = dp[i-5] +1
    elif i > 3 and dp[i-3] > 0:
        dp[i] = dp[i-3]+1
print(dp[n])