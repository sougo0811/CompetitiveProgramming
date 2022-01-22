import collections

N = int(input())
AN = list(map(int,input().split()))
M = 200000
BN = list(range(1,200001))
cnt = 0
ans = [20001]

c = collections.Counter(AN)
c = dict(c)
max_k_list = [kv[0] for kv in c.items() if kv[1] == max(c.values())]
#print(max_k_list)

for i in (max_k_list):
  if cnt <= i:
    tmp = [j for j in AN if j != i]
    if ans >= tmp:
      ans = tmp
      cnt = i


ans = " ".join(map(str,ans))
print(ans)
