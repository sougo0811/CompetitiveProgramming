#A
'''
N = int(input())
if 1<=N and N<=125:
  print(4)
elif 126<=N and N<=211:
  print(6)
elif 212<=N and N<=214:
  print(8)
'''
#B
'''
S,T = map(int,input().split())
a = []
b = []
c = []
count = 0
for i in range(S+1):
  a.append(i)
  b.append(i) 
  c.append(i)
for x in a:
  for y in b:
    for z in c:
      if x+y+z<=S and x*y*z<=T:
        count += 1
print(count)
'''

#C

N = int(input())
Sn = map(int,input().split())
Tn = map(int,input().split())
S = list(Sn)
T = list(Tn)
gem = [T[0]]
n = 0
ST = 0
for t in T[1::]:
  ST += S[n]
  if t <= T[0]+ST:
    gem.append(t)
    n += 1
  else:
    gem.append(T[0]+ST)
    n += 1
for g in gem:
  print(g)

#D
'''
N = int(input())

'''
