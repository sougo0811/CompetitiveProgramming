N = int(input())
AN = list(map(int,input().split()))

AN = list(sorted(AN))
BN = list(range(1,N+1))
if AN == BN:
  print("Yes")
else:
  print("No")