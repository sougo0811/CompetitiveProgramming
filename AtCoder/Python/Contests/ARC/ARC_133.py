N = int(input())
AN = list(map(int,input().split()))
M = 200000
BN = list(range(1,200001))
cnt = 0
ans = [20001]
for i in range(N):
  if cnt <= AN.count(i):
    tmp = [j for j in AN if j != i]
    if ans >= tmp:
      ans = tmp
      cnt = AN.count(i)

ans = " ".join(map(str,ans))
print(ans)