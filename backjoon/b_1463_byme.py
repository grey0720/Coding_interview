'''
원래 DP인데 dfs 풀이
그런데 시간 복잡도 O(n^2)
백준은 통과함...
'''
import sys
input = sys.stdin.readline

n = int(input().strip())
count = 0
stack = [n]
while 1 not in stack:
    save = []
    for i in stack:    
        if i%3 == 0 and (i//3) not in save:
            save.append(i//3)
        if i%2 == 0 and (i//2) not in save:
            save.append(i//2)
        if (i-1) not in save:
            save.append(i-1)
    count += 1
    stack = save
print(count)