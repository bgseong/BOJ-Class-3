from collections import deque
import sys
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(start,vi,now):
    m_l=[]
    vi=vi[:]
    q=deque([start])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N or vi[nx][ny] != 0 or int(gr[nx][ny])>now:
                continue
            vi[nx][ny]=vi[x][y]+1
            q.append([nx,ny])
            if int(gr[nx][ny])<now and int(gr[nx][ny]) in [1,2,3,4,5,6]:
                m_l.append([[nx,ny],vi[nx][ny]])
    return sorted(m_l,key=lambda x:(x[1],x[0][0],x[0][1]))




N=int(sys.stdin.readline())

vi=[[0 for _ in range(N)]for __ in range(N)]
gr=[]
now=2
for _ in range(N):
    a=list(sys.stdin.readline().split())
    if "9" in a:
        for i in range(N):
            if a[i] == "9":
                x,y=_,i
    gr.append(a)
total=0
c=0
while 1:
    vi=[[0 for _ in range(N)]for __ in range(N)]
    a=bfs([x,y],vi,now)
    if a == []:
        break
    gr[a[0][0][0]][a[0][0][1]] = gr[x][y]
    gr[x][y] = 0
    x,y=a[0][0][0],a[0][0][1]
    c+=1
    total+=a[0][1]
    if c==now:
        c=0
        now+=1
print(total)
    



