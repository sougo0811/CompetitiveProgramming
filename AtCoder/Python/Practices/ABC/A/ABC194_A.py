A,B = map(int,input().split())
milk_k = A+B
milk_s = B
if milk_k >= 15 and milk_s >= 8:
  print(1)
elif milk_k >= 10 and milk_s >= 3:
  print(2)
elif milk_k >= 3:
  print(3)
else:
  print(4)