#A
'''
import itertools
S = input()
SL = [''.join(i) for i in itertools.permutations(S)]
SL = list(set(SL))
print(len(SL))
'''

#B
'''
import collections

N = int(input())
xy = [map(int, input().split()) for _ in range(N-1)]
x, y = [list(i) for i in zip(*xy)]
xys = []
for j in range(N-1):
  xys.append(x[j])
  xys.append(y[j])
xy_same = [k for k,v in collections.Counter(xys).items() if v == N-1]
if xy_same == []:
  print("No")
else:
  print("Yes")
'''

#C
'''
N, M = map(int,input().split()) 
B = [list(map(int, input().split())) for l in range(N)]
#print(B)
count = 0
for i in B[0]:
  if i%7 == 0:
    if B[0][-1]%7 != 0:
      count += 1
      break
    else:
      for j in range(N):
        for k in range(M-1):
          if B[j][k]+1 != B[j][k+1]:
            count += 1
            break
if count == 0:
    for j in range(N):
      for k in range(M-1):
        if B[j][k]+1 != B[j][k+1]:
          count += 1
          break
if count == 0:
  for m in range(N-1):
    if B[m][0]+7 != B[m+1][0]:
      count += 1
      break
if count == 0:
  print("Yes")
else:
  print("No")
'''

#D
N,Q = map(int,input().split())
query_list = [list(map(int,input().split())) for l in range(Q)]
print(query_list)