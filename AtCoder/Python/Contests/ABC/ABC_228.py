#A
'''
S,T,X = map(int,input().split())


if T < S:
  T += 24

flg = False
if S <= X < T:
  flg = True
elif S <= X+24 < T:
  flg = True


if flg == True:
  print("Yes")
else:
  print("No")
'''

'''
N, X = map(int, input().split())
AN = list(map(int, input().split()))
cnt = 1
A = [0]
A.extend(AN)
AN = A
flg = True
#print(AN)
knowman = AN[X]
knowmen = []
knowmen.append(X)
while flg == True:
  if AN[knowman] in knowmen:
    flg = False
    cnt += 1
    break
  else:
    cnt += 1
    knowmen.append(knowman)
    knowman = AN[knowman]
print(cnt)
'''

'''
N, X = map(int, input().split())
AN = list(map(int, input().split()))
flg = True
C = 0
klist = [X]
while flg == True:
    a = AN[X-1]
    if a in klist:
        flg = False
    else:
        X = a
        klist.append(X)
    if C == N:
        break
    C += 1
print(len(set(klist)))
12 5 7 14 20 10 3
'''

'''
n, x = map(int,input().split())
a = list(map(int,input().split()))

ans = []
c = 0
i = x-1
ans.append(x)
while x != a[i]:
  if c == n:
    break
  ans.append(a[i])
  i = a[i] - 1
  c += 1

print(len(set(ans)))
'''

#C