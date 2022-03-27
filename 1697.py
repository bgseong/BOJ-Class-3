import sys
from collections import deque

def bfs(start):
    q=deque([start])
    while q:
        n=q.popleft()
        if n<0 and n>100000:
            continue
        if n==M:
            print(gr[n])
            break
        for i in [n-1,n+1,n*2]:
            if 0 <= i <= 100000 and not gr[i]:
                gr[i]=gr[n]+1
                q.append(i)


N,M=map(int,sys.stdin.readline().split())

gr=[0 for i in range(100001)]
bfs(N)
