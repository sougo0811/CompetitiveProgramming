N = input()

def f(x):
  a = list(x)
  total = 0
  for i in a:
    total+=int(i)
  return total


#M = f(2*x)

print(f(2*N))