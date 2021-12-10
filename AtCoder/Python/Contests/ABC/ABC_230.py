#A
'''
N = int(input())

if 1 <= N <= 9:
  print("AGC00"+str(N))
elif 10 <= N < 42:
  print("AGC0"+str(N))
else:
  print("AGC0"+str(N+1))
'''

#B
'''
S = input()
list_S = list(S)
len_S = len(list(S))
out_list = ["oxo","xxx","oox","xoo","ooo"]
flg = True
if len_S <= 2:
  if S == "oo":
    print("No")
  else:
    print("Yes")
elif len_S == 3 and S in out_list:
  print("No")
else:
  for i in range(len_S-2):
    if S[i:i+3:] in out_list:
      print("No")
      flg = False
      break
    else:
      continue
  if flg == True:
    print("Yes")
'''