import sys

def sol(target):
    start=0
    end=len(li_s)-1
    while start <= end:
        mid = (start + end) // 2
        if li_s[mid] == target:
            return mid
        if li_s[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return None



N=int(sys.stdin.readline())
li=list(map(int,sys.stdin.readline().split()))
li_s=sorted(set(li))
for i in li:
    print(sol(i),end=" ")
