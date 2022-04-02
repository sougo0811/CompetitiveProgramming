#A
'''
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

if x1 == x2:
  x = x3
elif x2 == x3:
  x = x1
elif x3 == x1:
  x = x2

if y1 == y2:
  y = y3
elif y2 == y3:
  y = y1
elif y3 == y1:
  y = y2

print(str(x) + " " + str(y))
'''

#B
'''
A,B = map(int,input().split())

r = (A**2 + B**2)**0.5
cos = (A/r)
sin = (B/r)
print(str(cos)+" "+str(sin))
'''


#C
'''
N,K,X = map(int,input().split())
AN = list(map(int, input().split()))
BN = [AN[i]%X for i in range(N) if AN[i]%X < 0.5*X]
CN = [X-AN[i]%X for i in range(N) if AN[i]%X >= 0.5*X]
BN.extend(CN)
DN = list(zip(AN,BN))
DN = sorted(DN, reverse=False, key=lambda x: x[1])
print(DN)

for i in range(N):
  if K > 0:
    if (AN[i][0] + AN[i][1]) == X:
      a = (AN[i][0] + AN[i][1])/X
      
    elif (AN[i][0] - AN[i][1]) == X:
      a = (AN[i][0] - AN[i][1])/X
    if K - a >= 0:
      K -= a
'''

#D
'''
N = int(input())

def f(X):
  global flg
  a = 0
  b = 0
  while X >= a**3 + a**2*b + a*b**2 + b**3:
    while X >= a**3 + a**2*b + a*b**2 + b**3:
      if X == a**3 + a**2*b + a*b**2 + b**3:
        print(X)
        flg = False
        return flg
      a += 1
    a = 0
    b += 1

flg = True
X = N
while flg:
  f(X)
  X += 1
'''