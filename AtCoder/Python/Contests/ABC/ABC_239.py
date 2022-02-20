#A
'''
H = int(input())
ans = (H*(12800000+H))**0.5
print(ans)
'''
#B
'''
X = int(input())
ans = (X//10)
print(ans)
'''
#C
'''
x1,y1,x2,y2 = map(int,input().split())
if (x2,y2) == (x1+1+1,y1+2+2) or (x2,y2) == (x1+1+2,y1+2+1) or (x2,y2) == (x1+1-1,y1+2+2) or (x2,y2) == (x1+1-2,y1+2+1) or (x2,y2) == (x1+1-2,y1+2-1) or (x2,y2) == (x1+1-1,y1+2-2) or (x2,y2) == (x1+1+1,y1+2-2) or (x2,y2) == (x1+1+2,y1+2-1):
  print("Yes")
elif  (x2,y2) == (x1+2+1,y1+1+2) or (x2,y2) == (x1+2+2,y1+1+1) or (x2,y2) == (x1+2-1,y1+1+2) or (x2,y2) == (x1+2-2,y1+1+1) or (x2,y2) == (x1+2-2,y1+1-1) or (x2,y2) == (x1+2-1,y1+1-2) or (x2,y2) == (x1+2+1,y1+1-2) or (x2,y2) == (x1+2+2,y1+1-1):
  print("Yes")
elif  (x2,y2) == (x1-2+1,y1+2+2) or (x2,y2) == (x1-1+2,y1+2+1) or (x2,y2) == (x1-1-1,y1+2+2) or (x2,y2) == (x1-1-2,y1+2+1) or (x2,y2) == (x1-1-2,y1+2-1) or (x2,y2) == (x1-1-1,y1+2-2) or (x2,y2) == (x1-1+1,y1+2-2) or (x2,y2) == (x1-1+2,y1+2-1):
  print("Yes")
elif  (x2,y2) == (x1-2+1,y1+1+2) or (x2,y2) == (x1-2+2,y1+1+1) or (x2,y2) == (x1-2-1,y1+1+2) or (x2,y2) == (x1-2-2,y1+1+1) or (x2,y2) == (x1-2-2,y1+1-1) or (x2,y2) == (x1-2-1,y1+1-2) or (x2,y2) == (x1-2+1,y1+1-2) or (x2,y2) == (x1-2+2,y1+1-1):
  print("Yes")
elif  (x2,y2) == (x1-2+1,y1-1+2) or (x2,y2) == (x1-2+2,y1-1+1) or (x2,y2) == (x1-2-1,y1-1+2) or (x2,y2) == (x1-2-2,y1-1+1) or (x2,y2) == (x1-2-2,y1-1-1) or (x2,y2) == (x1-2-1,y1-1-2) or (x2,y2) == (x1-2+1,y1-1-2) or (x2,y2) == (x1-2+2,y1-1-1):
  print("Yes")
elif (x2,y2) == (x1+1+1,y1-2+2) or (x2,y2) == (x1+1+2,y1-2+1) or (x2,y2) == (x1+1-1,y1-2+2) or (x2,y2) == (x1+1-2,y1-2+1) or (x2,y2) == (x1+1-2,y1-2-1) or (x2,y2) == (x1+1-1,y1-2-2) or (x2,y2) == (x1+1+1,y1-2-2) or (x2,y2) == (x1+1+2,y1-2-1):
  print("Yes")
elif  (x2,y2) == (x1+2+1,y1-1+2) or (x2,y2) == (x1+2+2,y1-1+1) or (x2,y2) == (x1+2-1,y1-1+2) or (x2,y2) == (x1+2-2,y1-1-1) or (x2,y2) == (x1+2-2,y1-1-1) or (x2,y2) == (x1+2-1,y1-1-2) or (x2,y2) == (x1+2+1,y1-1-2) or (x2,y2) == (x1+2+2,y1-1-1):
  print("Yes")
else:
  print("No")
'''
#D

A,B,C,D = map(int,input().split())
Min = 10*5
Min_i = 0

def ispirme(n: int) -> bool:

    if n <= 1: return False

    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True

for i in range(C,D+1):
  l = [j for j in range(A+i,B+i+1) if ispirme(j)]
  l = len(l)
  if Min > l:
    Min = l
    Min_i = i

if Min > D-C:
  print("Takahashi")
else:
  print("Aoki")

'''
m = int(input())
def ispirme(n: int) -> bool:

    if n <= 1: return False

    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
primes = [i for i in range(m) if ispirme(i)]
print(primes)
'''