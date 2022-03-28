import sys

N,M=map(int,sys.stdin.readline().split())
gr=[]
for i in range(N):
    li=[]
    a=sys.stdin.readline().replace("\n","")
    for j in a:
        li.append(int(j))
    gr.append(li)
q=[[0,0]]
while q:
    x,y=q.pop(0)
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    if x == N-1 and y == M-1:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if gr[nx][ny] == 1:
            gr[nx][ny] = gr[x][y]+1
            q.append([nx,ny])
print(gr[N-1][M-1])
