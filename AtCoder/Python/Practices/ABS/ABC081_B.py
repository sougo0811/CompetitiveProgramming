N = int(input())
AN = list(map(int,input().split()))
flg = 0
cnt1 = 0
while flg == 0:
  cnt2 = 0
  for i in range(N):
    if AN[i]%2 == 0:
      AN[i] /= 2
      cnt2 += 1
      continue
    else:
      flg = 1
      break
  if cnt2 == N:
    cnt1 += 1
print(cnt1)