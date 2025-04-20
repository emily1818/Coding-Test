import sys 
from collections import Counter
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = {}
p1, p2 = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n+1)
cnt = 0 

m = int(input())
for i in range(m) :
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
def bfs(start, end) :
    queue = deque()
    #방문처리
    queue.append(start)
    visited[start] = 0


    while queue :
        current = queue.popleft()
        for ne  in graph[current] :
            if visited[ne] == -1:
                visited[ne] = visited[current] +1 
                queue.append(ne)
                if ne == end :
                    return 
                


bfs(p1, p2)
print(visited[p2] if visited[p2] != -1 else -1)