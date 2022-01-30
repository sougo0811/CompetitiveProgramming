#A
def resolve():
  '''
  N = int(input())
  if  -2**31<=N<2**31:
    print("Yes")
  else:
    print("No")
  '''
#B
  '''
  import numpy as np
  H,W = map(int,input().split())
  AHW = []
  for _ in range(H):
    AW = list(map(int,input().split()))
    AHW.append(AW)
  
  AHW_t = (np.array(AHW).T).tolist()
  for i in range(W):
    ans = " ".join(map(str,AHW_t[i]))
    print(ans)
  '''


'''
AHW_t = np.array(AHW).T
for i in AHW_t:
  print(*i)
'''