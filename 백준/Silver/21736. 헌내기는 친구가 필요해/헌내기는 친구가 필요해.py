import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
cnt = 0 

arr = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] == "O":
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif arr[nx][ny] == "P":
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1

# 시작점 찾기
for i in range(n): 
    for j in range(m):
        if arr[i][j] == "I":
            start_x, start_y = i, j
            bfs(start_x, start_y)

if cnt:
    print(cnt)
else:
    print("TT")
