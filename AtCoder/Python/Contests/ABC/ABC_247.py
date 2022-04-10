#A
'''
S = input()
S = list(S)

S.insert(0,0)
S.pop(-1)
S = "".join([str(n) for n in S])
print(S)
'''
#B
'''
N = int(input())
sN = []
tN = []
for _ in range(N):
  s,t = map(str,input().split())
  sN.append(s)
  tN.append(t)

flg = True

for i in range(N):
  sNc = list(sN)
  sNc.pop(i)
  tNc = list(tN)
  tNc.pop(i)
  if sN[i] in sNc:
    if tN[i] in sNc:
      flg = False
      break
    if tN[i] in tNc:
      flg = False
      break
  if sN[i] in tNc:
    a = [x for x in range(len(sN)) if sN[x] == tN[i]]
    for j in range(len(a)):
      if a[j] != i:
        if tN[i] != sN[a[j]]:
          flg = False
          break

if flg:
  print("Yes")
else:
  print("No")
'''

#C
'''
N = int(input())
S1 = "1"
S2 = S1+" "+"2"+" "+S1
S3 = S2+" "+"3"+" "+S2
S4 = S3+" "+"4"+" "+S3
S5 = S4+" "+"5"+" "+S4
S6 = S5+" "+"6"+" "+S5
S7 = S6+" "+"7"+" "+S6
S8 = S7+" "+"8"+" "+S7
S9 = S8+" "+"9"+" "+S8
S10 = S9+" "+"10"+" "+S9
S11 = S10+" "+"11"+" "+S10
S12 = S11+" "+"12"+" "+S11
S13 = S12+" "+"13"+" "+S12
S14 = S13+" "+"14"+" "+S13
S15 = S14+" "+"15"+" "+S14
S16 = S15+" "+"16"+" "+S15
s = [0,S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16]
ans = s[N]
print(ans)
'''
#D
Q = int(input())
query = []
for _ in range(Q):
  q = list(map(int,input().split()))
  query.append(q)

tutu = []

for i in range(Q):
  if query[i][0] == 1:
    for j in range(query[i][2]):
      tutu.append(query[i][1])
  elif query[i][0] == 2:
    cnt = 0
    for j in range(query[i][1]):
      cnt += tutu[0]
      tutu.pop(0)
    print(cnt)