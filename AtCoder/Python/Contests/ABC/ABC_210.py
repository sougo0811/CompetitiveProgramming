'''
N,A,X,Y = map(int,input().split())
if N < A:
  s = N * X
else:
  s = A * X + (N - A) * Y
print(s)
'''

'''
N = int(input())
S = str(input())
s = list(S)
count = 1
for i in s:
  if i == '1':
    if count%2 == 0:
      print('Aoki')
      break
    else:
      print('Takahashi')
      break
  elif i == '0':
    count += 1
'''

'''
N,K = map(int,input().split())
cn = list(map(int,input().split()))
point = 0
flg = 0
if N == K:
  cnl = list(set(cn))
  s = len(cnl)
  print(s)
else:
  for k in range(1,N-K):
    count = 0
    cnl = []
    for i in cn[k-1:]:
      cnl.append(i)
      count += 1
      if count == K:
        break
    cnl = list(set(cnl))
    s = len(cnl)
    if point < s:
      point = s
    if K == s:
      print(s)
      flg += 1
      break
  if flg < 1:
    print(s)
'''

'''
N,K = map(int,input().split())
 
c = list(map(int,input().split()))
 
ans = 0
cnt = {}
for i in range(K):
    if c[i] in cnt:
        cnt[c[i]] += 1
    else:
        cnt[c[i]] = 1
 
ans = len(cnt)   
 
for i in range(N-K):
    if cnt[c[i]] == 1:
        cnt.pop(c[i])
    else:
        cnt[c[i]] -= 1
    
    if c[i+K] in cnt:
        cnt[c[i+K]] += 1
    else:
        cnt[c[i+K]] = 1
    
    ans = max(ans,len(cnt))
 
print(ans)
'''