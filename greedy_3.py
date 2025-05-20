def solution(L):
    g = []
    for i in range(len(L)):
        g.append(min(L[i]))
    print(max(g))

l1 = [[3,1,2],
      [4,1,4],
      [2,2,2]]
l2 = [[7,3,1,8],
      [3,3,3,4]]
solution(l1)
solution(l2)