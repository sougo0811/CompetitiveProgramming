#A
'''
S = input()
if len(S) == 1:
  print(S*6)
elif len(S) == 2:
  print(S*3)
else:
  print(S*2)
'''

#B
'''
import itertools
N,W = map(int,input().split())
AN = list(map(int,input().split()))
one = AN
two = []
three = []

one = list(set(one))
one = [x for x in one if x<=W]

if len(AN) >= 2:
  two = list(itertools.combinations(AN, 2))
  AN_two = [i[0]+i[1] for i in two]
  AN_two = list(set(AN_two))
  two = [x for x in AN_two if x<=W]
if len(AN) >= 3:
  three = list(itertools.combinations(AN, 3))
  AN_three = [j[0]+j[1]+j[2] for j in three]
  AN_three = list(set(AN_three))
  three = [x for x in AN_three if x<=W]

num = len(set(one + two + three))
print(num)
'''

#C
'''
N = int(input())
SN = []
TN = []
STN = []
S_MAX = ""
T_MAX = 0
MAX_cnt = 0
cnt = 0
for _ in range(N):
  cnt += 1
  S,T = map(str,input().split())
  SN = list(set(SN))
  if T_MAX < int(T):
    if S not in SN:
      T_MAX = int(T)
      MAX_cnt = cnt
  SN.append(S)
print(MAX_cnt)
'''

#D
'''
W = int(input())
print(297)
for i in range(1,100):
  print(i,end=" ")
  print(i*100,end=" ")
  print(i*10000,end=" ")
'''