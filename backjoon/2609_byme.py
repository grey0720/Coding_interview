'''
이정도는 뭐 C 껌이지~~
최소공배수 & 최대공약수 문제
'''
import os, sys
input = sys.stdin.readline

n, m = map(int, input().split())
def gcd(a,b):
    min_val = min(a,b)
    for i in range(min_val, 1, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1
g = gcd(n,m)
print(g)
print(n*m // g)