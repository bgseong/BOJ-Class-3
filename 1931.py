import sys
from collections import deque

li=deque()
N=int(sys.stdin.readline())
for i in range(N):
  li.append(list(map(int,sys.stdin.readline().split())))

li=sorted(li,key=lambda x:(x[1],x[0]))
time=li[0][1]
count=1
for i in range(1,N):
  if time <= li[i][0]:
    time = li[i][1]
    count+=1
print(count)
