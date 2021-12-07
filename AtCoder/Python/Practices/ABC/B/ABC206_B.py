N = int(input())
money_box = 0
day = 1
while money_box < N:
  money_box += day
  day += 1
print(day-1)