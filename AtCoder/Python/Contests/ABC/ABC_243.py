#A
'''
V,A,B,C = map(int,input().split())
flg = True
while flg:
  if V < A:
    print("F")
    flg = False
    break
  V -= A
  if V < B:
    print("M")
    flg = False
    break
  V -= B
  if V < C:
    print("T")
    flg = False
    break
  V -= C
'''
#B
'''
N = int(input())
AN = list(map(int,input().split()))
BN = list(map(int,input().split()))
cnt_a =0
cnt_b = 0
A_N = []
B_N = []

for i in range(N):
  if AN[i] == BN[i]:
    cnt_a += 1
  else:
    A_N.append(AN[i])
    B_N.append(BN[i])

print(cnt_a)
for i in range(len(A_N)):
  if A_N[i] in B_N:
    cnt_b += 1
print(cnt_b)
'''
#C
'''
import copy

N = int(input())
XN = []
YN = []
XYN = []

for _ in range(N):
  x,y = map(int,input().split())
  XN.append(x)
  YN.append(y)
  #xy = [y,x]
  #XYN.append(xy)
S = list(input())
S = [-1 if S[i] == "R" else -2 for i in range(N)]

box = [[YN[i],False,False] for i in range(N)]
box = list(map(list, set(map(tuple, box))))
box_memory = copy.deepcopy(box)


for i in range(N):
  if S[i] == -1:
    box[box_memory.index([YN[i],False,False])][1] = True
  elif S[i] == -2:
    box[box_memory.index([YN[i],False,False])][2] = True
  point = [XN[i],S[i]]
  box[box_memory.index([YN[i],False,False])].append(point)

flg = True

for i in range(len(box)):
  if len(box[i]) > 4 and box[i][1] and box[i][2]:
    ok_R = 10**9
    ok_L = 0
    for j in range(3,len(box[i])):
      if box[i][j][1] == -1 and ok_R >= box[i][j][0]:
        ok_R = box[i][j][0]
      elif box[i][j][1] == -2 and ok_L <= box[i][j][0]:
        ok_L = box[i][j][0]
    if ok_R - ok_L <= 0:
      flg = False


if flg:
  print("No")
else:
  print("Yes")
'''

def Yes():
  print("Yes")
  exit(0)
N = int(input())
X, Y = [], []
for _ in range(N):
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)
S = input()
right_min, left_max = dict(), dict()
for i in range(N):
  if S[i] == 'R':
    if Y[i] in left_max and X[i] < left_max[Y[i]]:
      Yes()
  else:
    if Y[i] in right_min and right_min[Y[i]] < X[i]:
      Yes()
  if S[i] == 'R':
    if Y[i] in right_min:
      right_min[Y[i]] = min(X[i], right_min[Y[i]])
    else:
      right_min[Y[i]] = X[i]
  else:
    if Y[i] in left_max:
      left_max[Y[i]] = max(X[i], left_max[Y[i]])
    else:
      left_max[Y[i]] = X[i]
print("No")