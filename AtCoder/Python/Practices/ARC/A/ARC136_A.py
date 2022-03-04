N = int(input())
S = list(input())

def AtoBB(n):
  S[n] = "B"
  S.insert(n+1,"B")

def BBtoA(n):
  S[n] = "A"
  S.pop(n+1)

