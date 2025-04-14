import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
cnt = 0

arr = [list(input().strip()) for _ in range(n)]

def bfs(x, y):
    global cnt
    queue = [(x, y)]
    arr[x][y] = "X"  # 방문 처리

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == "O":
                    arr[nx][ny] = "X"
                    queue.append((nx, ny))
                elif arr[nx][ny] == "P":
                    arr[nx][ny] = "X"
                    queue.append((nx, ny))
                    cnt += 1

# 시작점 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == "I":
            bfs(i, j)

if cnt:
    print(cnt)
else:
    print("TT")
