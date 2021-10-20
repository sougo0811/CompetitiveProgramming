#A
'''
N = list(map(int,input()))
while len(N) <= 3:
  N.insert(0,0)
N = [str(a) for a in N[0:4]]
N = "".join(N)
print(N)
'''
#B
'''
N,P = map(int,input().split())
an = list(map(int, input().split()))
count = 0
for a in an:
  if a < P:
    count += 1
print(count)
'''
#C
'''
N,M = map(int,input().split())
a = [list(map(str,input().split())) for l in range(N*2)]
print(a)
'''
#D
'''
import itertools
N = int(input())
an = list(map(int,input().split()))
bn = list(map(int,input().split()))
abn = list(zip(an,bn))
#print(abn[0])
cn = []
for ab in abn:
  s = list(itertools.combinations_with_replacement(range(ab[0],ab[1]+1),N))
  if len(s) >= 2:
    s.pop()
  cn.extend(s)
  print(s)
cn = list(set(s))
print(len(cn)%998244353)
'''