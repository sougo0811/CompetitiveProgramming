#A
'''
N = int(input())
S = list(input())

if S[N-1] == "o":
  print("Yes")
else:
  print("No")
'''

#B
'''
P = list(map(int,input().split()))
alf_dict = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
S = []
for i in P:
  if i in alf_dict:
    S.append(alf_dict[i])
S = "".join(S)
print(S)
'''

#C
'''
N = int(input())
S = []
for i in range(N):
  S.append(list(input().split()))
#for a in range(N):
  #print(S[i])
T = []
for i in range(N):
  T.append(list(input().split()))
#for a in range(N):
  #print(T[i])
'''

#D
N = int(input())
xn = []
yn = []
for i in range(N):
  x,y = map(int,input().split())
  xn.append(x)
  yn.append(y)
#print(xn,yn)
a = ""
b = ""
c = ""
d = ""
for i in range(N):
  a = (xn[i],yn[i])
  for j in range(N):
    b = (xn[j],yn[j])
    if a == b:
      break
    for k in range(N):
      c = (xn[k],yn[k])
      if a == c:
        break
      if b == c:
        break
      for l in range(N):
        d = (xn[l],yn[l])
        if a == d:
          break
        if b == d:
          break
        if c == d:
          break
        print(a,b,c,d)