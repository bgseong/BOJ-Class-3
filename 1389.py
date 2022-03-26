import sys
from collections import deque

def bfs(start):
    if v[start] == 0:
        v[start] = 1
        for i in g[start]:
            if v[i] == 0:
                if i not in hi:
                    num[i] = num[start]+1
                    hi.append(i)
        if hi != deque():
            bfs(hi.popleft())




N,M=map(int,sys.stdin.readline().split())

vi=[0]*(N+1)
gr=[[]]
for i in range(N):
    gr.append([])
for i in range(M):
    x,y=map(int,sys.stdin.readline().split())
    gr[x].append(y)
    gr[y].append(x)
for i in range(len(gr)):
    gr[i].sort()
sums={}
for i in range(1,N+1):
    num=[]
    for J in range(N+1):
        num.append(0)
    g=list(gr)
    v=list(vi)
    hi = deque()
    bfs(i)
    sums[i] = sum(num)
print((sorted(sums.items(),key=lambda x:(x[1],x[0])))[0][0])
