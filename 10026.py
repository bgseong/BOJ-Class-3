import sys
sys.setrecursionlimit(10**6)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(start,gr):
  if vi[start[0]][start[1]] == 1:
    return False
  vi[start[0]][start[1]] = 1
  for i in range(4):
    nx=start[0]+dx[i]
    ny=start[1]+dy[i]
    if nx<0 or nx>=N or ny<0 or ny>=N:
      continue
    if gr[nx][ny] == gr[start[0]][start[1]]:
      dfs([nx,ny],gr)
  return True

N=int(sys.stdin.readline())

nom=[]
yak=[]
for i in range(N):
  z=sys.stdin.readline().replace("\n","")
  p=[]
  for j in z:
    p.append(j)
  nom.append(p)
  z=z.replace("G","R")
  p=[]
  for j in z:
    p.append(j)
  yak.append(p)

vi=[[0 for _ in range(N)] for _ in range(N)]
c=0
for i in range(N):
  for j in range(N):
    if dfs([i,j],nom):
      c+=1
print(c)
vi=[[0 for _ in range(N)] for _ in range(N)]
c=0
for i in range(N):
  for j in range(N):
    if dfs([i,j],yak):
      c+=1
print(c)

