A1,A2,A3 = map(int,input().split())
A = [A1,A2,A3]
Ar = sorted(A)
if Ar[2]-Ar[1] == Ar[1]-Ar[0]:
  print("Yes")
else:
  print("No")