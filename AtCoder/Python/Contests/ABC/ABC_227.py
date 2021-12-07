#A
'''
N,K,A = map(int,input().split())

persons = list(range(1,N+1))
B = A-1
for i in range(K):
  B+=1
if B >= N:
  B%=N
print(persons[B-1])
'''

#B
'''
N = int(input())
S = list(map(int, input().split()))
S = sorted(S)
SN = [4*a*b+3*a+3*b for a in range(1,S[-1]) for b in range(1,S[-1]) if 4*a*b+3*a+3*b <= S[-1] ]
SN = list(sorted(set(SN)))
count = 0
for i in range(N):
    if not S[i] in SN:
        count+=1
print(count)
#print(SN)
'''

#C
'''
from itertools import combinations_with_replacement

N = int(input())
Ns = ((a,b,c) for a,b,c in combinations_with_replacement(range(1,N+1),3) if a<=b<=c and a*b*c<=N)
a = sum(1 for _ in Ns)
print(a)
'''

#C
'''
n=int(input())
count=0
for a in range(1,n+1):
    if a*a*a > n:
        break
    for b in range(a,n+1):
        if a*b*b >n:
            break
        count+=n//a//b -b+1
print(count)
'''

#D
'''
import random
N,K = map(int,input().split())
AN = list(map(int, input().split()))
count = 0
flg = N
ANS = sorted(AN)
while flg >= K:
  a = []
  for j in range(K):
      k = flg-1
      k-=j
      a.append(k)
  small_cnt = 0
  for i in a:
    if ANS[i] == 0:
      flg -= 1
      ANS.remove(0)
      break
    else:
      ANS[i] -= 1
      small_cnt += 1
  if small_cnt == K:
    count += 1
      
print(count)
'''