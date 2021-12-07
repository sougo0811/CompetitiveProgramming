N = int(input())
AN = list(map(int,input().split()))

count = 0
for i in AN:
  if i <= 10:
    continue
  else:
    i -= 10
    count += i
print(count)