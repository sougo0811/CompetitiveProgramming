#A
'''
N = int(input())
S = list(input())
flg = True

for i in range(N-1):
  if S[i] != S[-i-1]:
    if S[i] == "B":
      if i == 0:
        S[-i-2] = "A"
        S[-i-1] = "B"
      else:
        S[i] = "A"
        S[i+1] = "B"
    else:
      if i != 0 and S[-i-1] == "B":
        S[-i-1] = "A"
        S[-i] = "B"
      else:
        flg = False
#S="".join(S)
#print(S)
if flg:
  print("Yes")
else:
  print("No")
'''

N = int(input())
S = list(input())
SS = "".join(S)
if S[0] != S[-1] and S[-1] == "B":
  print("No")
else:
  if SS != "BA":
    print("Yes")
  else:
    print("No")