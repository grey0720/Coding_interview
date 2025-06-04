'''
greedy
input.strip()은 지피티 사용
이외는 무난히 성공
'''
import sys
input = sys.stdin.readline

li = list(map(int, input().strip()))
stack = 0
for i in li:
    if stack == 0:
        stack += i
    else:
        stack = max(stack + i, stack * i)
print(stack)