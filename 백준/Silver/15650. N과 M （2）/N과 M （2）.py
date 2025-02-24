import sys
input = sys.stdin.readline

n, m = map(int, input().split())
res = []

def dfs(x):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    for i in range(x, n+1):
        if i not in res:
            res.append(i)
            dfs(i + 1)
            res.pop()
dfs(1)
#push 확인
n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)
 