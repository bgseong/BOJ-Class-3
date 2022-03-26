import sys
sys.setrecursionlimit(10**7)
def sol(start):
    if vi[start] == 0:
        vi[start] = 1
        for num in gr[start]:
            sol(num)
        return True
    return False


N,M=map(int,sys.stdin.readline().split())
gr=[]
vi=[]
for i in range(N+1):
    gr.append([])
    vi.append(0)
for i in range(M):
    x,y=map(int,sys.stdin.readline().split())
    gr[x].append(y)
    gr[y].append(x)
c=0
for i in range(1,N+1):
    if sol(i):
        c+=1
print(c)
