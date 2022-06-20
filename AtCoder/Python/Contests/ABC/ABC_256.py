#A
'''
N = int(input())
print(2**N)
'''

#B
'''
N = int(input())
AN = list(map(int,input().split()))
x = [0]*8
P = 0
a = 0; b = 0; c = 0; d = 0
for i in range(N):
  if AN[i] == 1:
    x[0]+=1
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    x[0] = 0
    x[1] = a
    x[2] = b
    x[3] = c
    x[4] = d
    P += x[4]
  elif AN[i] == 2:
    x[0]+=1
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    x[0] = 0
    x[1] = 0
    x[2] = a
    x[3] = b
    x[4] = c
    x[5] = d
    P += x[4]+x[5]
  elif AN[i] == 3:
    x[0]+=1
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    x[0] = 0
    x[1] = 0
    x[2] = 0
    x[3] = a
    x[4] = b
    x[5] = c
    x[6] = d
    P += x[4]+x[5]+x[6]
  else:
    x[0]+=1
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    x[0] = 0
    x[1] = 0
    x[2] = 0
    x[3] = 0
    x[4] = a
    x[5] = b
    x[6] = c
    x[7] = d
    P += x[4]+x[5]+x[6]+x[7]
  x[4]=0;x[5]=0;x[6]=0;x[7]=0

print(P)
'''
#