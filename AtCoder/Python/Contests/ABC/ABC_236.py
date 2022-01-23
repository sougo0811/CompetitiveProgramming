#A
'''
S = input()
S = list(S)
a,b = map(int,input().split())

A = S[a-1]
B = S[b-1]
S[a-1] = B
S[b-1] = A
S = "".join(S)
print(S)
'''
#B
'''
import collections
N = int(input())
AN = list(map(int,input().split()))

c = dict(collections.Counter(AN))
ans = min(c.items(), key = lambda x:x[1])[0]
print(ans)
'''
#C
'''
N,M = map(int,input().split())
SN = list(map(str,input().split()))
TM = list(map(str,input().split()))
UM = sorted(TM)

def binary_search(data, value):
    left = 0            # 探索する範囲の左端を設定
    right = len(data) - 1            # 探索する範囲の右端を設定
    while left <= right:
        mid = (left + right) // 2            # 探索する範囲の中央を計算
        if data[mid] == value:
            # 中央の値と一致した場合は位置を返す
            return mid
        elif data[mid] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = mid - 1
    return -1     

for i in range(N):
  data = UM
  value = SN[i]
  ans = binary_search(data, value)
  if ans == -1:
    print("No")
  else:
    print("Yes")
'''
'''
for i in range(N):
  if SN[i] in TM:
    print("Yes")
  else:
    print("No")
'''

#D
N = int(input())
ANN = []
for _ in range(1,2*N):
  AN = list(map(int,input().split()))
  ANN.append(AN)

