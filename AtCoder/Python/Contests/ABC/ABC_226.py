#A
'''
from decimal import Decimal, ROUND_HALF_UP
X = float(input())
print(Decimal(str(X)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
'''

#B
'''
N = int(input())
a = [[] for i in range(N)]
for j in range(N):
  LN = []
  LN = list(map(int,input().split()))
  a[j] = LN
#print(a)
for k in range(N):
  a[k][0] = 0
a = list(map(list, set(map(tuple, a))))
print(len(a))
'''

#C
N = int(input())
a = [[] for i in range(N)]
for j in range(N):
  KN = []
  KN = list(map(int,input().split()))
  a[j] = KN
#print(a)
time = a[N-1][0]
WZN = a[N-1]
WZK = a[N-1][1]
for i in range(WZK):
  Ki = a[i][1]
  time += a[i][0]
  a[i][0] = 0
  if Ki == 0:
    continue
  else:
    for ki in range(Ki):
      time += a[WZN[ki+2]+1][0]
      a[WZN[ki+2]+1][0] = 0
      if a[WZN[ki+2]+1][1] == 0:
        continue
      else:
        for ji in range(a[WZN[ki+2]+1][1]):
          time += a[WZN[ji+2]+1][0]
          a[WZN[ji+2]+1][0] = 0
print(time)
