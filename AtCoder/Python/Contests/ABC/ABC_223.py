#A
'''
X = (int(input()))
if X == 0:
  print("No")
else:
  if X%100 == 0:
    print("Yes")
  else:
    print("No")
'''

#B
'''
S = input()
S = list(S)
SS = []
for i in range(len(S)):
  S.append(S[0])
  del S[0]
  StrS = "".join(S)
  SS.append(StrS)
SS = sorted(SS)
print(SS[0])
print(SS[-1])
'''

#C
'''
N = (int(input()))
AB = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]
times =[]
total_time = 0
for i in range(N):
  time = A[i] / B[i]
  times.append(time)
  total_time += time
half_time = total_time/2
s = 0
long = 0
for j in range(N):
  s += times[j]
  long += A[j]
  if s > half_time:
    s-= times[j]
    long -= A[j]
    remain = half_time - s
    remain = remain*B[j]
    long += remain
    break
print(long)
'''

#D
'''
import itertools
N,M = map(int,input().split())
AB = [map(int, input().split()) for _ in range(M)]
A, B = [list(i) for i in zip(*AB)]
NLS = list(itertools.permutations(range(1,N+1)))
print(NLS)
'''