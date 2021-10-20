'''
A,B = map(int,input().split())
if A == 0:
  S = 'Silver'
elif B == 0:
  S = 'Gold'
else:
  S = 'Alloy'
print(S)
'''

'''
ipt = input()
X = [int(i) for i in list (ipt)]
if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
  S = 'Weak'
else:
  S = 'Strong'
if X[0] < 6:
  if [X[0],X[1],X[2],X[3]] == [X[0],X[0]+1,X[0]+2,X[0]+3]:
    S = 'Weak'
elif X[0] == 7:
  if X == [7,8,9,0]:
    S = 'Weak'
elif X[0] == 8:
  if X == [8,9,0,1]:
    S = 'Weak'
elif X[0] == 9:
  if X == [9,0,1,2]:
    S = 'Weak'
else:
  S = 'Strong'
print(S)
'''

'''
N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
ans = float('inf')
i = 0
j = 0
while i < N and j < M:
  x = abs(A[i] - B[j])
  ans = min(ans,x)
  if ans == 0:
      break
  if A[i] < B[j]:
    i += 1
  else:
    j += 1
print(ans)
'''

