#A
'''
A,B = map(int,input().split())
print(A^B)
'''

#B
N = int(input())
AN = list(map(int, input().split()))
AN2 = sorted(AN, reverse = True)
for a in range(N):
    if AN[a] == AN2[1]:
        print(a+1)