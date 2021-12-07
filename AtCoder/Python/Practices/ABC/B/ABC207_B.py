A,B,C,D = map(int,input().split())
count = 0
M = A
R = 0
while M > R*D and count != -1:
  count += 1
  M += B
  R += C
  if B >= C*D:
      count = -1
print(count)
