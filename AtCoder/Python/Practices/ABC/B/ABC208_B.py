import math

P = int(input())
count = 0
while P!=0:
  for i in range(1,P+2):
    if math.factorial(i) > P:
      j = i-1
      for k in range(1,100):
        if math.factorial(j)*k > P:
          l = k-1
          count += l
          P -= (math.factorial(j)*l)
          break
      break
print(count)
