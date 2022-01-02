#A
'''
S = input()
S = list(S)
print(int(S[0])*int(S[2]))
'''

'''
S = input()
T = input()
alf = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
S = list(S)
T = list(T)
S0 = alf.index(S[0])
T0 = alf.index(T[0])
ST = (S0 - T0+26)%26
flg = True
for i in range(len(S)):
  if ST == (alf.index(S[i]) - alf.index(T[i])+26)%26:
    flg = True
  else:
    flg = False
    break
if flg == True:
  print("Yes")
else:
  print("No")
'''

#C
N,M = map(int,input().split())
if M == 0:
  print("Yes")
else:
  AB = [map(int, input().split()) for _ in range(M)]
  A, B = [list(i) for i in zip(*AB)]
  CD = [map(int, input().split()) for _ in range(M)]
  C, D = [list(i) for i in zip(*CD)]
  numAB = [0,0,0,0,0,0,0,0,0]
  numCD = [0,0,0,0,0,0,0,0,0]
  for i in range(N):
    if 1 == A[i]:
      numAB[1] += 1
    elif 2 == A[i]:
      numAB[2] += 1
    elif 3 == A[i]:
      numAB[3] += 1
    elif 4 == A[i]:
      numAB[4] += 1
    elif 5 == A[i]:
      numAB[5] += 1
    elif 6 == A[i]:
      numAB[6] += 1
    elif 7 == A[i]:
      numAB[7] += 1
    elif 8 == A[i]:
      numAB[8] += 1
    if 1 == B[i]:
      numAB[1] += 1
    elif 2 == B[i]:
      numAB[2] += 1
    elif 3 == B[i]:
      numAB[3] += 1
    elif 4 == B[i]:
      numAB[4] += 1
    elif 5 == B[i]:
      numAB[5] += 1
    elif 6 == B[i]:
      numAB[6] += 1
    elif 7 == B[i]:
      numAB[7] += 1
    elif 8 == B[i]:
      numAB[8] += 1
    if 1 == C[i]:
      numCD[1] += 1
    elif 2 == C[i]:
      numCD[2] += 1
    elif 3 == C[i]:
      numCD[3] += 1
    elif 4 == C[i]:
      numCD[4] += 1
    elif 5 == C[i]:
      numCD[5] += 1
    elif 6 == C[i]:
      numCD[6] += 1
    elif 7 == C[i]:
      numCD[7] += 1
    elif 8 == C[i]:
      numCD[8] += 1
    if 1 == D[i]:
      numCD[1] += 1
    elif 2 == D[i]:
      numCD[2] += 1
    elif 3 == D[i]:
      numCD[3] += 1
    elif 4 == D[i]:
      numCD[4] += 1
    elif 5 == D[i]:
      numCD[5] += 1
    elif 6 == D[i]:
      numCD[6] += 1
    elif 7 == D[i]:
      numCD[7] += 1
    elif 8 == D[i]:
      numCD[8] += 1
  numAB = sorted(numAB)
  numCD = sorted(numCD)
  if numAB == numCD:
    print("Yes")
  else:
    print("No")
