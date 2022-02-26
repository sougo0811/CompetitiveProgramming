#A
'''
a = list(map(int,input().split()))
b = a[0]
c = a[b]
d = a[c]
print(d)
'''

#B
'''
N,M = map(int,input().split())
AN = list(map(int,input().split()))
BN = list(map(int,input().split()))

flg = 0
for i in range(M):
  if BN[i] in AN:
    AN.remove(BN[i])
  else:
    flg += 1
    break
if flg == 0:
  print("Yes")
else:
  print("No")
'''
#C
'''
N = int(input())
SN = [list(input()) for i in range(N)]
flg = 0
for i in range(N):
  for j in range(N):
    if N-j >= 6 and SN[i][j] == "#":
      point = 2
      for a in range(5):
        if SN[i][j+1+a] == ".":
          point -= 1
        if a == 4 and point >= 0:
          flg += 1
          break
    elif N-j >= 6 and SN[i][j] == ".":
      point = 1
      for a in range(5):
        if SN[i][j+1+a] == ".":
          point -= 1
        if a == 4 and point >= 0:
          flg += 1
          break
    if N-i >= 6 and SN[i][j] == "#":
      point = 2
      for a in range(5):
        if SN[i+1+a][j] == ".":
          point -= 1
        if a == 4 and point >= 0:
          flg += 1
          break
    elif N-i >= 6 and SN[i][j] == ".":
      point = 1
      for a in range(5):
        if SN[i+1+a][j] == ".":
          point -= 1
        if a == 4 and point >= 0:
          flg += 1
          break
    if N-i >= 6 and N-j >= 6 and SN[i][j] == "#":
      point = 2
      for a in range(5):
        if SN[i+1+a][j+1+a] == ".":
          point -= 1
        if a == 4 and point >= 0:
          flg += 1
          break
    elif N-i >= 6 and N-j >= 6 and SN[i][j] == ".":
      point = 1
      for a in range(5):
        if SN[i+1+a][j+1+a] == ".":
          point -= 1
        if a == 4 and point >= 0:
          flg += 1
          break
    if N-i >= 6 and j >= 5 and SN[i][j] == "#":
      point = 2
      for a in range(5):
        if SN[i+1+a][j-1-a] == ".":
          point -= 1
        if a == 4 and point >= 0:
          flg += 1
          break
    elif N-i >= 6 and j >= 5 and SN[i][j] == ".":
      point = 1
      for a in range(5):
        if SN[i+1+a][j-1-a] == ".":
          point -= 1
        if a == 4 and point >= 0:
          flg += 1
          break

if flg > 0:
  print("Yes")
else:
  print("No")
'''

#D
'''
import bisect
A = []
Q = int(input())
query = [list(map(int,input().split())) for i in range(Q)]
#print(query)

for i in range(Q):
  if query[i][0] == 1:
    bisect.insort(A,query[i][1])
  elif query[i][0] == 2:
    n = bisect.bisect(A,query[i][1])
    if n < query[i][2]:
      print(-1)
    else:
      B = A[0:n]
      print(B[-query[i][2]])
  else:
    n = (len(A)-bisect.bisect(A,query[i][1]))
    if n < query[i][2]:
      print(-1)
    else:
      B = A[bisect.bisect(A,query[i][1]):]
      print(B[query[i][2]-1])
'''