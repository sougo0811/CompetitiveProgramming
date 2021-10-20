#A
'''
X = int(input())
if 0 <= X < 40:
  print(40-X)
elif 40 <= X < 70:
  print(70-X)
elif 70 <= X < 90:
  print(90-X)
else:
  print("expert")
'''
#B
'''
S1 = input()
S2 = input()
S3 = input()
T = input()
S = ""
for i in T:
  if i == "1":
    S += S1
  elif i == "2":
    S += S2
  elif i == "3":
    S += S3
print(S)
'''
#C
'''
X = input()
N = int(input())
str_list = [input() for _ in range(N)]
alf = ["0","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alf_new = list(X)
dict_alf = dict(zip(alf, alf_new))
str_list.sort(dict_alf)
print(str_list)
'''
#C
X = input()
N = int(input())
S = [None] * N
for i in range(N):
  S[i] = input()

d = {}
xx = 0
for i in X:
  d[i] = xx
  xx = xx + 1
  
table = str.maketrans({**d})

S_N = sorted(S, key=lambda ss : (ss.translate(table), ss))

for i in S_N:
  print(i)