N = int(input())
if N%100 == 0:
  N = N//100
else:
  N = N//100+1
print(N)