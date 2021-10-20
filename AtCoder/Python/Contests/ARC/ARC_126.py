#A
T = int(input())
case = [None] * T
for i in range(T):
  case[i] = list(map(int,(input().split())))

count_list = []



'''
for i in case:
  count = 0
  long = 0
  i2 = 1
  n = 0
  for j in i:
    i2 += 1 
    while j > 0:
      long = j*(i2)
      if long == 10:
        count += 1
      elif long < 10:
        for j2 in i[n//3+1]:
          while j2 > 0:
            long += j2*((i2//3)+1)
            if long == 10:
              count += 1
            elif long < 10:
              for j3 in case[(i+2)//3]:
                while j3 > 0:
                  long += j3*((i2//3)+2)
                  if long == 10:
                    count += 1
                  else:
                      j3 -= 1
            else:
                j2 -= 1
      else: j -= 1
  count_list.append(count)
print(count_list)
'''