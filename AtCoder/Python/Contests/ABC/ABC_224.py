#A
'''
S = input()
S = list(S)
if S[-2] == "e" and S[-1] == "r":
  print("er")
else:
  print("ist")
'''

#B
'''
import itertools
H,W = map(int,input().split())
A = [list(map(int, input().split())) for l in range(H)]

rows = list(itertools.combinations(range(1,H+1),2))
lines = list(itertools.combinations(range(1,W+1),2))
rls = list((itertools.product(rows,lines)))
count = 0
for rl in rls:
  if A[rl[0][0]-1][rl[1][0]-1] + A[rl[0][1]-1][rl[1][1]-1] <= A[rl[0][1]-1][rl[1][0]-1] + A[rl[0][0]-1][rl[1][1]-1]:
    continue
  else:
    count-=1
    break
if count == 0:
  print("Yes")
else:
  print("No")
'''

#C
'''
N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
'''