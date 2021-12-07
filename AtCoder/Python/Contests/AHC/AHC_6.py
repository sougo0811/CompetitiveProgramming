'''
import random
N = 1000
a = [0] * N
b = [0] * N
c = [0] * N
d = [0] * N
for i in range(N):
  a[i], b[i], c[i], d[i]= map(int, input().split())

long_list = []
long_list.append(102)
x1 = 400
y1 = 400
long_list.append(x1)
long_list.append(y1)
long_x = 0
long_y = 0
T = 0

num = list(range(1,1001))
roots = random.sample(num,50)

for j in range(50):
  xi = a[roots[j]]
  yi = b[roots[j]]
  long_list.append(xi)
  long_list.append(yi)
  long_x = abs(x1 - xi)
  long_y = abs(y1 - yi)
  time = long_x + long_y
  T += time

x1 = a[roots[49]]
y1 = b[roots[49]]

for k in range(50):
  xi = c[roots[k]]
  yi = d[roots[k]]
  long_list.append(xi)
  long_list.append(yi)
  long_x = abs(x1 - xi)
  long_y = abs(y1 - yi)
  time = long_x + long_y
  T += time

m = []
m.append(50)
rm = roots
imrm = m+rm
mrm = [str(a) for a in imrm]
mrm = " ".join(mrm)
print(mrm)

long_list.append(400)
long_list.append(400)
slong_list = [str(b) for b in long_list]
slong_list = " ".join(slong_list)
print(slong_list)
'''

'''
N = 1000
a = [0] * N
b = [0] * N
c = [0] * N
d = [0] * N
for i in range(N):
  a[i], b[i], c[i], d[i]= map(int, input().split())

nlm = 0
long_list = []
long_list.append(102)
x1 = 400
y1 = 400
long_list.append(x1)
long_list.append(y1)
long_x = 0
long_y = 0
T = 0
while nlm != 50:
  xi = a[nlm]
  yi = b[nlm]
  long_list.append(xi)
  long_list.append(yi)
  long_x = abs(x1 - xi)
  long_y = abs(y1 - yi)
  time = long_x + long_y
  T += time
  nlm += 1

x1 = a[50]
y1 = b[50]
nlm = 0
while nlm != 50:
  xi = c[nlm]
  yi = d[nlm]
  long_list.append(xi)
  long_list.append(yi)
  long_x = abs(x1 - xi)
  long_y = abs(y1 - yi)
  time = long_x + long_y
  T += time
  nlm += 1

m = []
m.append(50)
rm = list(range(1,51))
imrm = m+rm
mrm = [str(a) for a in imrm]
mrm = " ".join(mrm)
print(mrm)

long_list.append(400)
long_list.append(400)
slong_list = [str(b) for b in long_list]
slong_list = " ".join(slong_list)
print(slong_list)

#44637
'''