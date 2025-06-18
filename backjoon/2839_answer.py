import sys
input = sys.stdin.readline

n = int(input)
dp = [5001] * (n+1)
dp[0] = 0

for i in range(3, n+1):
    if i >= 3 :
        dp[i] = min(dp[i], dp[i-3]+1)
    if i >= 5:
        dp[i] = min(dp[i], dp[i-5]+1)

print(dp[n] if dp[n] != 5001 else -1) ## python 식 삼항 연산자