#A
'''
S = input()
S = list(S)
S = sorted(S)
if S[-1] == "8":
  print(9)
else:
  for j in range(9):
    if int(S[j]) != j:
      print(j)
      break
'''
#B
'''
A,B,K = map(int,input().split())
cnt = 0
while A < B:
  A*=K
  cnt+=1
print(cnt)
'''

#C
import itertools
import math


N,M,K = map(int,input().split())
l = [i for i in range(1,M+1)]
a = list(itertools.product(l,repeat=N))
#b = [j for j in range(len(a)) if sum(a[j]) <= K]
print(len(a))


#D


