N = int(input())
d = []
for _ in range(N):
  d.append(int(input()))

d = list(sorted(set(d)))
print(len(d))