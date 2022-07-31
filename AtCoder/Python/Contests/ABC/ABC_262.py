#A
'''
Y = int(input())

if Y % 4 == 2:
  print(Y)
elif Y % 4 == 1:
  print(Y+1)
elif Y % 4 == 0:
  print(Y+2)
else:
  print(Y+3)
'''

#B
'''
N,M = map(int,input().split())
UVM = [[False] * N for _ in range(N)]
for _ in range(M):
  U,V = map(int,input().split())
  U-=1;V-=1
  UVM[U][V] = True
  UVM[V][U] = True

cnt = 0

for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      if UVM[i][j] and UVM[j][k] and UVM[k][i]:
        cnt += 1

print(cnt)
'''
#C
N = int(input())
AN = list(map(int,input().split()))

for i in range(N):
  AN[i] -= 1
same = 0
for (i,x) in enumerate(AN):
  if i == x:
    same += 1
ans = same * (same - 1) // 2

for (i,j) in enumerate(AN):
  if i < j and AN[j] == i:
    ans += 1

print(ans)