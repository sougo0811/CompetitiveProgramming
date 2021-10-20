#A
'''
XY = float(input())
X = int(XY)
Y = XY - X
Y = int(Y*10)
if Y>=0 and Y<=2:
  print(str(X)+"-")
elif 3<=Y and Y<=6:
  print(str(X))
elif 7<=Y and Y<=9:
  print(str(X)+"+")
'''
#B
'''
N = int(input())
namelist = []
for i in range(0,N):
  S,T = map(str,input().split())
  name = S,T
  if name:
    namelist.append(name)
count = 0
for n in namelist:
  for m in namelist:
    if n == m:
      count += 1
    else:
      count += 0
if count >= N+1:
  print("Yes")
else:
  print("No")
'''

#C
N = int(input())
n = 0
m = N
t = 2
long = 121
if N<=120:
  print("A"*N)
else:
  while long >= 120:
    while N//t >= 1:
      N /= t
      n += 1
    ans = ("A"*(t-1)+"B"*n + "A"*int(m-t**n))
    long = len(ans)
    t += 1
    N = m
    n = 0
  print(ans)