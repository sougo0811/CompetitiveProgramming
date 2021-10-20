#A
'''
A,B = map(int,input().split())
BA = A - B
M = 32**BA
print(M)
'''

#B
'''
import copy
S = input()
n = len(S)
S = list(S)
T = list(input())
t = copy.copy(T)
count = 0
if S == T:
  print("Yes")
else:
  for i in range(0,n-1):
    T[i],T[i+1] = T[i+1],T[i]
    if S == T:
      count += 1
    else:
      T = copy.copy(t)
  if count >= 1:
    print("Yes")
  else:
    print("No")
'''

#C
'''
import itertools
N = input()
n = len(N)
N = list(N)
for i in range(len(N)):
  N[i] = int(N[i])
print(N)

for pt in itertools.permutations(N,n):
  pt = list(pt)
  for i in range(n):
    onebox = pt[n]
  print(list(pt))
'''

#D
N = int(input())
l = [list(map(int, input().split())) for l in range(N)]
print(l)
for i in range(N):
  AB = l[i]
  for j in range(AB[0],AB[0]+AB[1]-1):
#N個空リスト作成+それぞれの日数入れる+
