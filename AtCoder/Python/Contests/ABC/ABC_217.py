#A
'''
S,T = map(str,input().split())
if S < T:
  print("Yes")
else:
  print("No")
'''
#B
'''
S1 = str(input())
S2 = str(input())
S3 = str(input())

S = [S1,S2,S3]
abc = 0
arc = 0
agc = 0
ahc = 0

for s in S:
  if s == "ABC":
    abc += 1
  elif s == "ARC":
    arc += 1
  elif s == "AGC":
    agc += 1
  elif s == "AHC":
    ahc += 1
if abc == 0:
  print("ABC")
if arc == 0:
  print("ARC")
if agc == 0:
  print("AGC")
if ahc == 0:
  print("AHC")
'''

#C
'''
N = int(input())
P = list(map(int,input().split()))
Key = sorted(P)
P = dict(zip(Key,P))
#print(P)
P = sorted(P.items(), key=lambda x:x[1])
#print(P)
P = dict(P)
Q = []
for q in P.keys():
  Q.append(q)
Q = [str(a) for a in Q]
Q = " ".join(Q)
print(Q)
'''

#D
L,Q = map(int,input().split())
C = []
X = []
wood_key = []
wood_value = []
for i in range(0,L):
  wood_key.append(i)
  wood_value.append(L)

for q1 in range(0,Q):
  c,x = map(int,input().split())
  C.append(c)
  X.append(x)
CX = [C,X]
#print(C,X)
c = 0
x = 0
for q2 in range(0,Q):
  if C[q2] == 1:
    cut = X[q2]
    while X[q2] > 0:
      wood_value[X[q2]-1] = cut
      X[q2]-= 1
    X[q2]=cut
  elif C[q2] == 2:
    print(wood_value[X[q2]])


#for q2 in enumerate(CX):
  #print(q2)
  #if q2[1] == 1:
    #wood_key[]
