N,L,R = map(int,input().split())

x = 0
for i in range(1,N*N):
  if L <= i <= R and (i^N) < N:
    x += 1
print(x)