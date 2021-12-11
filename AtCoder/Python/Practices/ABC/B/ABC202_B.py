S = input()
Sr = list(S)[::-1]
ans = []
for i in Sr:
  s = i
  if i == "6":
    s = 9
  elif i == "9":
    s = 6
  ans.append(s)
for i in ans:
    print(i,end = '')