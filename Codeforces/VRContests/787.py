#A
'''
t = int(input())
tlist = []
for _ in range(t):
  abcxy = list(map(int,input().split()))
  tlist.append(abcxy)

for i in range(t):
  a = tlist[i][0]
  b = tlist[i][1]
  c = tlist[i][2]
  x = tlist[i][3]
  y = tlist[i][4]
  flg = False
  dog_ok = a - x
  cat_ok = b - y
  if dog_ok >= 0:
    flg = True
  else:
    c += dog_ok
    if c >= 0:
      flg = True
  if cat_ok >= 0:
    flg = True
  else:
    c += cat_ok
    if c >= 0:
      flg = True
  if flg and c >= 0:
    print("YES")
  else:
    print("NO")
'''

#B
import copy
t = int(input())
for i in range(t):
  n = int(input())
  an = list(map(int,input().split()))
  an_new = copy.deepcopy(an)
  if an[-1] < len(an)-1:
    print(-1)
  elif an == sorted(an_new):
    print(0)
  else:
    cnt = 0
    flg = True
    while flg:
      an_new = copy.deepcopy(an)
      av = max(an)
      if av == an[-1]:
        av = sorted(an)[-2]
      for k in range(1,n-1):
        if av <= an[-1]//(2**k):
          av = sorted(an)[-(k+2)]
      if len(an) != len(list(set(an))):
        dup = sorted([x for x in set(an) if an.count(x) > 1])
        av = dup[0]
      ai = an.index(av)
      av = av//2
      an[ai] = av
      cnt += 1
      #print(an)
      if an == sorted(an) and an == list(set(an)):
        print(cnt)
        flg = False
        break
      if sorted(an)[-1] < len(an)-1:
        print(-1)
        flg = False
        break
      if an == an_new:
        flg = False
        break