'''
구현 문제
제한시간 20분
txt 파일 이용해서 두개 다 실행 중
txt 파일 읽어오는 함수 잘 기억해둘 것
'''

import sys, os
import time

start = time.time()
# input = sys.stdin.readline
# 현재 파일 기준으로 한 단계 위 디렉토리
## 파일 읽어오는 코드이니 잘 숙지해둬야 함
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
# 한 단계 위에 있는 data.txt 파일 경로
file_path = os.path.join(parent_dir, 'input.txt')

li = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        t  = line.strip()
        ## strip() : 개행문자 제거
        li.append(t)
print(li)
for m in li:
    m = list(map(int, m))
    l = len(m)

    if sum(m[0:(l//2)]) == sum(m[l//2:]):
        print("LUCKY")
    else:
        print("READY")
end = time.time()
print(end-start)