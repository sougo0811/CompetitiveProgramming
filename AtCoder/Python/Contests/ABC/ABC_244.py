#A
'''
N = int(input())
S = input()
S = list(S)
print(S[-1])
'''

#B
'''
N = int(input())
T = input()
T = list(T)

x = 0
y = 0
rad = 1
for i in range(N):
  if T[i] == "S":
    if rad%4 == 1:
      x += 1
    elif rad%4 == 2:
      y -= 1
    elif rad%4 == 3:
      x -= 1
    else:
      y += 1
  else:
    rad += 1
print(str(x)+" "+str(y))
'''

#C
'''
N = int(input())
flg = True
ok_list = list(range(1,2*N+2))
while flg:
  if len(ok_list) == 0:
    flg = False
    break
  print(ok_list[0])
  ok_list.pop(0)
  N = int(input())
  if N == 0:
    flg = False
    break
  ok_list.remove(N)
'''

#D
'''
S1,S2,S3 = map(str,input().split())
T1,T2,T3 = map(str,input().split())
RGB = ["GRB","BGR","RBG"]
RBG = ["BRG","GBR","RGB"]
BRG = ["RBG","GRB","BGR"]
BGR = ["GBR","RGB","BRG"]
GRB = ["RGB","BRG","GBR"]
GBR = ["BGR","RBG","GRB"]
S = S1+S2+S3
T = T1+T2+T3
if S == 'RGB':
  if T in GRB:
    print("Yes")
  else:
    print("No")
elif S == 'RBG':
  if T in BRG:
    print("Yes")
  else:
    print("No")
elif S == 'BRG':
  if T in RBG:
    print("Yes")
  else:
    print("No")
elif S == 'BGR':
  if T in GBR:
    print("Yes")
  else:
    print("No")
elif S == 'GRB':
  if T in RGB:
    print("Yes")
  else:
    print("No")
elif S == 'GBR':
  if T in BGR:
    print("Yes")
  else:
    print("No")
'''

#E
N,M,K,S,T,X = map(int,input().split())
UM = []
VM = []
for _ in range(M):
  U,V = map(int,input().split())
  UM.append(U)
  VM.append(V)

