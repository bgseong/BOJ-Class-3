import sys
sys.setrecursionlimit(10**7)
from collections import deque
def dfs(start):
    if vi_d[start] == 0:
        print(start,end=" ")
        vi_d[start] = 1
        for i in gr_d[start]:
            dfs(i)

def bfs(start):
    if vi_b[start] == 0:
        print(start, end=" ")
        vi_b[start] = 1
        for i in gr_b[start]:
            if vi_b[i] == 0:
                if i not in hi:
                    hi.append(i)
        if hi != deque():
            bfs(hi.popleft())




N,M,V=map(int,sys.stdin.readline().split())

vi_d=[0]*(N+1)
gr_d=[[]]
for i in range(N):
    gr_d.append([])
for i in range(M):
    x,y=map(int,sys.stdin.readline().split())
    gr_d[x].append(y)
    gr_d[y].append(x)
for i in range(len(gr_d)):
    gr_d[i].sort()

gr_b=list(gr_d)
vi_b=list(vi_d)
dfs(V)
print("")
hi=deque()
bfs(V)
