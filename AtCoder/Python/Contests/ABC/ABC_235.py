#A
'''
abc = input()

abc = list(abc)
bca = []
bca.append(abc[1])
bca.append(abc[2])
bca.append(abc[0])
cab = []
cab.append(abc[2])
cab.append(abc[0])
cab.append(abc[1])
abc = int("".join(abc))
bca = int("".join(bca))
cab = int("".join(cab))
print(abc+bca+cab)
'''

#B
'''
N = int(input())
HN = list(map(int,input().split()))

hight = 0
for i in range(N):
  if HN[i] > hight:
    hight = HN[i]
  else:
    break

print(hight)
'''

#C

N,Q = map(int,input().split())
aN = list(map(int,input().split()))
xk = [map(int, input().split()) for _ in range(Q)]
x, k = [list(i) for i in zip(*xk)]
xk = list(zip(x,k))

#TEL
'''
for i in range(Q):
  q = xk[i][0]
  ok_cnt = xk[i][1]
  cnt = 0
  total = 0
  flg = False
  for j in range(N):
    total += 1
    if aN[j] == q:
      cnt += 1
    if ok_cnt == cnt:
      print(total)
      flg = True
      break
  if flg == False:
    print(-1)
'''



#D
'''
a,N = map(int,input().split())
'''



