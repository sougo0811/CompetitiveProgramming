#A
'''
L1,R1,L2,R2 = map(int,input().split())
if L1 <= L2:
  if R1 >= R2:
    print(R2-L2)
  elif R1 >= L2:
    print(R1-L2)
  else:
    print(0)
else:
  if R2 >= R1:
    print(R1-L1)
  elif R2 >= L1:
    print(R2-L1)
  else:
    print(0)
'''

#B
'''
import numpy as np
N = int(input())
ANN = []
for i in range(N):
  AN = list(input())
  ANN.append(AN)
 
BNN = np.array(ANN).T
BNN = np.array(BNN).tolist()
 
flg = True
 
for j in range(N):
  for k in range(N):
    a = ANN[j][k]
    b = BNN[j][k]
    if a == "W":
      if b != "L":
        print("incorrect")
        flg = False
        break
    if a == "L":
      if b != "W":
        print("incorrect")
        flg = False
        break
    if a == "D":
      if b != "D":
        print("incorrect")
        flg = False
        break
  if flg == False:
    break
if flg:
  print("correct")
'''
#C
'''
from collections import Counter
N = int(input())
SN = []
for i in range(N):
  S = input()
  SN.append(S)
SN_ans = Counter(SN)
SN_ans_c = SN_ans.copy()
#print(SN_ans)
for j in range(N):
  S_ans = SN[j]
  #print(SN_ans_c[S_ans] - SN_ans[S_ans])
  if SN_ans_c[S_ans] - SN_ans[S_ans] == 0:
    print(S_ans)
    SN_ans[S_ans] = SN_ans[S_ans] - 1
  else:
    print(S_ans + "(" + str(SN_ans_c[S_ans] - SN_ans[S_ans]) + ")")
    SN_ans[S_ans] = SN_ans[S_ans] - 1
'''

#D

N,M = map(int,input().split())
XN = list(map(int,input().split()))
CM = [];YM = []
for i in range(M):
  C,Y = map(int,input().split())
  CM.append(C);YM.append(Y)

cnt = 0