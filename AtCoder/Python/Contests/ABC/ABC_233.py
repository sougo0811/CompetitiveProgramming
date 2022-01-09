#A
'''
import math
X,Y = map(int,input().split())
if Y - X > 0:
  print(math.ceil((Y-X)/10))
else:
  print(0)
'''

#B
'''
L,R = map(int,input().split())
S = list(input())

PoPS = S[L-1:R]
RevS = reversed(PoPS)
S[L-1:R] = RevS
S = "".join(S)
print(S)
'''

#C
N,X = map(int,input().split())
L_AN = [list(map(int,input().split())) for _ in range(N)]
L = [L_AN[i][0] for i in range(N)]
AN_LN = [ L_AN[i][1:] for i in range(N)]
print(L)
print(AN_LN)