#A
'''
A,B,C = map(int,input().split())
BA = B-A
if BA/C >= 1:
  if (BA//C*C) >= A:
    print(BA//C*C)
  else:
    print((BA//C*C)+C)
else:
  print(-1)
'''

'''
AC
A,B,C=map(int,input().split())
for i in range(A,B+1):
  if i%C==0:print(i);exit()
print(-1)
'''

#B
'''
K = int(input())
A,B = map(int,input().split())
def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(str(X)[-i])*(n**(i-1))
    return out
a = Base_n_to_10(A,K)
b = Base_n_to_10(B,K)
print(a*b)
'''
