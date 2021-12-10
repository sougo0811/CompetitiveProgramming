#A
'''
S1 = input()
S2 = input()

S1 = list(S1)
S2 = list(S2)
if S1[0] == "." and S2[1] == ".":
  print("No")
elif S1[1] == "." and S2[0] == ".":
  print("No")
else:
  print("Yes")
'''

#B
'''
A,B = map(str,input().split())
A = list(A)
B = list(B)
lA = len(A)
lB = len(B)
len_s = 0
flg = False
if lA < lB:
  len_s = lA
else:
  len_s = lB
rA = list(reversed(A))
rB = list(reversed(B))
for i in range(0,len_s):
  if int(rA[i])+int(rB[i]) >= 10:
    print("Hard")
    flg = True
    break
if flg == False:
  print("Easy")
'''