'''
greedy
input.strip()은 지피티 사용
이외는 이것도 무난히 성공
'''
import sys
input = sys.stdin.readline

st = list(input().strip())
stack = {'0':0, '1':0}
str = ''
for s in st:
    if str == '':
        str += s
    else:
        if str[-1] == s:
            str += s
        else:
            if s == '1':
                stack['0'] +=1
            else:
                stack['1']+=1
        str = s

print(max(stack['0'], stack['1']))