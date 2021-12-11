#A
'''
D = int(input())
P = D/100
print(P)
'''

#B
'''
import collections
N = int(input())
S = []
for _ in range(N):
  S.append(input())
S_count = collections.Counter(S)
max_kv = [kv[0] for kv in S_count.items() if kv[1] == max(S_count.values())]
print(max_kv[0])
'''

#C
'''
import collections
N,Q = map(int,input().split())
A = list(map(int, input().split()))
X = []
for _ in range(Q):
  X.append(int(input()))
A_count = collections.Counter(A)

for i in range(Q):
  cnt = 0
  cnt = [ v for k,v in A_count.items() if k >= X[i]]
  print(sum(cnt))
'''

N,Q=map(int,input().split())
A=[(a,10**9) for a in map(int,input().split())]
X=[]
for i in range(Q):
  x=int(input())
  X.append((x,i))

AX=sorted(A+X)[::-1]

ans=[0]*Q
cnt=0
for x,i in AX:
  if i<Q:
    ans[i]=cnt
  else:
    cnt+=1

print(*ans,sep="\n")


