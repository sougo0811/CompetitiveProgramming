#A
'''
t = int(input())

def f(x):
  return x**2+2*x+3

ans = f(f(f(t)+t)+f(f(t)))

print(ans)
'''
#B
'''
N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
x.append(x[0])
y.append(y[0])
max_ans = 0
for i in range(N):
  for j in range(N):
    max = (((x[i])-(x[j]))**2 + ((y[i])-(y[j]))**2)**(1/2)
    if max >= max_ans:
      max_ans = max

print(max_ans)
'''

#C
'''
K = int(input())

two = list(bin(K))
two = two[2:]
Int_two = int("".join(two))*2
print(Int_two)
'''

#D
import bisect
N,K = map(int,input().split())
PN = list(map(int,input().split()))

Pi = sorted(PN[:K])
for i in range(N-K+1):
  Max_K = Pi[-K]
  print(Max_K)
  if i != N-K:
    bisect.insort(Pi,PN[K+i])

'''
cnt = 0
k = K
while k >= 2:
  k /= 2
  cnt += 1

Pi = sorted(PN[:K+1])
Max_K = Pi[-K]

cut = 0.5
cut_flg = 0
for i in range(N):
  if cnt >= 1 and PN[K+i+1] <= Pi[len(Pi)//cut]:
    cnt -= 1
    cut /= 2
    cut_flg = 1
  elif cnt >= 1 and PN[K+i+1] > Pi[len(Pi)//cut]:
    cnt -= 1
    cut += cut / 2
    cut_flg = 2
  else:
    if cut_flg == 0:
      Pi.insert(len(Pi))
    elif cut_flg == 1:
      Pi.insert((len(Pi)//cut*2), )
    elif cut_flg == 2:
      Pi.insert(len(Pi)//(cut-(cut*2)))
'''