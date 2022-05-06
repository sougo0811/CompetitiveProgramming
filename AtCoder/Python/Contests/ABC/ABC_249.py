#A

A,B,C,D,E,F,X = map(int,input().split())
t_long = 0
a_long = 0
for i in range(X):
  if i%(A+C) <= A:
    t_long += B
  if i%(D+F) <= D:
    a_long += E

if t_long > a_long:
  print("Takahashi")
elif t_long < a_long:
  print("Aoki")
else:
  print("Draw")
'''

#B
'''
S = input()
S = list(S)
SS = list(set(S))
Lcnt = 0
Hcnt = 0
for i in range(len(S)):
  if S[i].islower():
    Lcnt += 1
  else:
    Hcnt += 1
if Lcnt != 0 and Hcnt != 0 and len(S) == len(SS):
  print("Yes")
else:
  print("No")

#C