N,X = map(int,input().split())
AN = list(map(int,input().split()))
for a in range(N):
  if a%2 == 0:
    X -= AN[a]
  else:
    X -= (AN[a]-1)
if X >= 0:
  print('Yes')
else:
  print('No')