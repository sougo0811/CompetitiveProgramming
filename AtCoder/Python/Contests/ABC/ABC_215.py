#A
'''
S = input()
if S == "Hello,World!":
  print("AC")
else:
  print("WA")
'''

#B
'''
N = int(input())
k = 0
while 2**k <= N:
  k+=1
print(k-1)
'''

#C
'''
import itertools

S,K = list(input().split()) 
K = int(K)
ans_list = list(itertools.permutations(S))
ans_set = sorted(set(ans_list))
print(''.join(ans_set[K-1]))
'''