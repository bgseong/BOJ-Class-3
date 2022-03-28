import sys
from collections import deque
sys.setrecursionlimit(10**7)
def dfs(y,x):
    count=0
    if gr[x][y] != 1:
        return 0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q=[[x,y]]
    while q:
        x,y=q.pop(0)
        if gr[x][y] == 1:
            count+=1
            gr[x][y] = 2
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or nx>=N or ny<0 or ny>=N:
                    continue
                if gr[nx][ny] == 1:
                    q.append([nx,ny])
    return count



N=int(sys.stdin.readline())
gr=[]
for i in range(N):
    li=[]
    for j in sys.stdin.readline().replace("\n",""):
        li.append(int(j))
    gr.append(li)
li=deque()
for i in range(N):
    for j in range(N):
        li.append(dfs(i,j))
li=deque(sorted(li))

for i in range(len(li)):
    if li[0] == 0:
        li.popleft()
print(len(li))
for i in li:
    print(i)

