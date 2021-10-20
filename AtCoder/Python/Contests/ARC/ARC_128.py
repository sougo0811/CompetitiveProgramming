#A
import time

import itertools
N = (int(input()))
As = list(map(int,input().split()))

time_sta = time.time()
#As_max = max(As)
#As_min = min(As)
#max_gold = As_max/As_min
total_gold = 0
max_acts = []
for i in itertools.product(range(0,2), repeat=N):
  acts = list(i)
  gold = 1
  silver = 0
  for j in range(N):
    if acts[j] == 1 and gold != 0 :
      silver = gold*As[j]
      gold = 0
    elif acts[j] == 1 and gold == 0:
      gold = silver/As[j]
      silver = 0
  if total_gold < gold:
    total_gold = gold
    max_acts = acts
#  if total_gold == max_gold:
#    break
max_acts = [str(a) for a in max_acts]
max_acts =" ".join(max_acts)
print(max_acts)

time_end = time.time()
print(time_end - time_sta)