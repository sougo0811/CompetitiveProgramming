#A

A,B = map(int,input().split())
coin = 0
for i in range(1,3):
  if A >= B:
    coin += A
    A -= 1
  else:
    coin += B
    B -= 1
print(coin)