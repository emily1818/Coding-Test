import sys
from collections import deque


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
graph = []

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < m and 0<= ny < n and graph[ny][nx] == 1 :
                queue.append((nx, ny))
                graph[ny][nx] = graph[y][x] + 1

for i in range(n) :
    graph.append(list(map(int, input().strip())))

bfs(0, 0)

print(graph[n-1][m-1])
            