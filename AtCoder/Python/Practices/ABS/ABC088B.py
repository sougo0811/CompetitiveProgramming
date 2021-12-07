N = int(input())
AN = list(map(int,input().split()))

Alice = 0
Bob = 0
AN = list(sorted(AN, reverse=True))
for i in range(N):
  if i%2 == 0:
    Alice += AN[i]
  else:
    Bob += AN[i]
print(Alice-Bob)