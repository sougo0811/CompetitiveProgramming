#A
'''
S = input()
f = S.count(S[0])
s = S.count(S[1])
t = S.count(S[2])
if f == 1:
  print(S[0])
elif s == 1:
  print(S[1])
elif t == 1:
  print(S[2])
else:
  print(-1)
'''

#B
'''
N,X,Y,Z = map(int,input().split())
AN = list(map(int,input().split()))
BN = list(map(int,input().split()))
CN = []

for i in range(N):
  C = [N-i,AN[i],BN[i],AN[i]+BN[i]]
  CN.append(C)
#print(CN)

CN = sorted(CN, reverse=True, key=lambda x: (x[1],x[0]))
XN = CN[0:X]
#print(CN)
CN = CN[X:]
CN = sorted(CN, reverse=True, key=lambda x: (x[2],x[0]))
YN = CN[0:Y]
#print(CN)
CN = CN[Y:]
CN = sorted(CN, reverse=True, key=lambda x: (x[3],x[0]))
ZN = CN[0:Z]
#print(CN)
WN = []
WN.extend(XN)
WN.extend(YN)
WN.extend(ZN)
WN = sorted(WN, reverse=True, key=lambda x: x[0])
for j in WN:
  print(N+1-j[0])
'''

N,X,Y = map(int,input().split())
