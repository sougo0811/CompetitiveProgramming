N,A,B = map(int,input().split())
sum = 0
for i in range(1,N+1):
  a = list(str(i))
  val = 0
  for j in a:
    val += int(j)
  if A <= val <= B:
    sum += int(i)
    val = 0
print(sum)