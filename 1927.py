import sys, heapq
from collections import deque
li=[]


N=int(sys.stdin.readline())
for Z in range(N):
  M=int(sys.stdin.readline())
  if M==0:
    if li==[]:
      print(0)
    else:
      print(heapq.heappop(li))
  else:
    heapq.heappush(li,M)
