'''
greedy
그리디 알고리즘으로 잘 작성함
무난히 통과 가능할듯?
'''
import sys
input = sys.stdin.readline

n = int(input().strip())
m = list(map(int, input().split()))
m.sort(reverse=True)
count = 0
while len(m) > 0:
    if m[0] <= len(m):
        l = m[0]
        count += 1
        m = m[l:]
    else:
        break
    print(m, l)
print(count)