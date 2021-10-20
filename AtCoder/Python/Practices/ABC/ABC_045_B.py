#B

SA = list(input())
SB = list(input())
SC = list(input())

turn = "A"
while SA != [] or SB != [] or SC != []:
  if turn == "A":
    if SA == []:
      win = "A"
      break
    if SA[0] == "a":
      turn = "A"
    elif SA[0] == "b":
      turn = "B"
    elif SA[0] == "c":
      turn = "C"
    del SA[0]
  elif turn == "B":
    if SB == []:
      win = "B"
      break
    elif SB[0] == "a":
      turn = "A"
    elif SB[0] == "b":
      turn = "B"
    elif SB[0] == "c":
      turn = "C"
    del SB[0]
  elif turn == "C":
    if SC == []:
      win = "C"
      break
    elif SC[0] == "a":
      turn = "A"
    elif SC[0] == "b":
      turn = "B"
    elif SC[0] == "c":
      turn = "C"
    del SC[0]

print(win)
