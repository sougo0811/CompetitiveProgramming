#A
'''
a,b = map(int,input().split())
if a == 10 and b == 1:
  print("Yes")
elif b == 10 and a ==1:
  print("Yes")
elif abs(b - a) == 1:
  print("Yes")
else:
  print("No")
'''
#B
'''
N = int(input())
AN = list(map(int,input().split()))
AN = list(set(AN))
print(len(AN))
'''
#C
'''
N,X = map(int,input().split())
AN = []
BN = []
for _ in range(N):
  A,B = map(int,input().split())
  AN.append(A)
  BN.append(B)
'''
#D
N = int(input())
AN = list(map(int,input().split()))
BN = []
BN.append(AN[0])
cnt = 1
print(len(BN))
for i in range(N-1):
  if len(BN) == 0:
    BN.append(AN[i+1])
    cnt = 1
    print(len(BN))
  else:
    if BN[-1] != AN[i+1]:
      BN.append(AN[i+1])
      cnt = 1
      print(len(BN))
    else:
      cnt += 1
      if cnt == AN[i+1]:
        for j in range(cnt-1):
          del BN[-1]
        cnt = 0
        if len(BN) == 0:
          cnt = 1
        else:
          b = BN[-1]
          for k in range(1,len(BN)+1):
            if b == BN[-k]:
              cnt += 1
            else:
              break
      else:
        BN.append(AN[i+1])
      print(len(BN))