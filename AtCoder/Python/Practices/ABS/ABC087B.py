import itertools

A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0

def calc_500(a):
  return a*500

def calc_100(b):
  return b*100

def calc_50(c):
  return c*50

a = range(A+1)
As = list(map(calc_500, a))
b = range(B+1)
Bs = list(map(calc_100, b))
c = range(C+1)
Cs = list(map(calc_50, c))
alls = list(itertools.product(As,Bs,Cs))
for all in alls:
  if sum(all) == X:
    count+=1
print(count)
