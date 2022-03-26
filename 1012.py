import sys
sys.setrecursionlimit(10**7)
def sol(x,y):
    if x<=-1 or x==N or y<=-1 or y==M:
        return False
    if gl[x][y] == 1:
        gl[x][y] = 0
        sol(x-1,y)
        sol(x+1, y)
        sol(x, y-1)
        sol(x, y+1)
        return True
    return False



T=int(sys.stdin.readline())
for Z in range(T):
    M,N,K=map(int,sys.stdin.readline().split())
    gl=[]
    for i in range(N):
        gl.append([0]*M)
    for ZZ in range(K):
        y,x=map(int,sys.stdin.readline().split())
        gl[x][y]=1
    re=0
    for i in range(M):
        for j in range(N):
            if sol(j,i):
                re+=1
    print(re)
