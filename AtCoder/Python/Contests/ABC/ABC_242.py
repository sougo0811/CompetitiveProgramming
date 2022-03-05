#A
'''
A,B,C,X = map(int,input().split())

if X <= A:
  print(1)
elif A+1 <= X <= B:
  ans = C/(B-A)
  print(ans)
else:
  print(0)
'''

#B
'''
S = list(input())
S = sorted(S)
S = "".join(S)
print(S)
'''


#C
from sympy import false


N = int(input())
ans = 0
for i in range(10**(N-1),10**(N)):
  a = list(str(i))
  if "0" not in a:
    flg = False
    for j in range(N-1):
      if abs(int(a[j]) - int(a[j+1])) <= 1:
        flg = True
      else:
        flg = False
        break
    if flg:
      ans += 1
print(ans%998244353)

#D
'''
S = input()
Q = int(input())
tQ = []
kQ = []
for _ in range(Q):
  t,k = map(int,input().split())
  tQ.append(t)
  kQ.append(k)
'''