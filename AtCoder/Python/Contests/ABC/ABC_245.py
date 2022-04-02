#A
'''
A,B,C,D= map(int,input().split())
if A < C:
  print("Takahashi")
elif A == C:
  if B <= D:
    print("Takahashi")
  else:
    print("Aoki")
else:
  print("Aoki")
'''
#B
'''
N = int(input())
AN = list(map(int,input().split()))
AN = sorted(list(set(AN)))
i = 0
while True:
  if i not in AN:
    print(i)
    break
  else:
    i += 1
'''
#C

N,K = map(int,input().split())
AN = list(map(int,input().split()))
BN = list(map(int,input().split()))

flg = True
for i in range(N):
  if AN[i] - AN[i+1]:
    print("")


#D

