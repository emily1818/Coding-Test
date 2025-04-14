#DFS 버전
import sys
sys.setrecursionlimit(10000) 

input = sys.stdin.readline

T = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def DFS(x, y) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<=nx<M) and (0<=ny<N) :
            if arr[nx][ny] == 1 : 
                arr[nx][ny] = 0 
                DFS(nx, ny) 

for _ in range(T) :
    cnt =0 
    M, N, K = map(int, input().split())
    arr = [[0] * (N) for _ in range(M)]

    #행렬 만들기
    for _ in range(K) :
        x, y = map(int, input().split())
        arr[x][y] = 1

    for x in range(M) :
        for y in range(N) :
            if arr[x][y] == 1:
                DFS(x, y)
                cnt += 1 
    print(cnt)





# #BFS 버전
# import sys
# input = sys.stdin.readline

# T = int(input())

# dx = [1, 0, -1, 0]
# dy = [0, -1, 0, 1]

# def BFS(x, y) :
#     queue = [(x, y)]
#     arr[x][y] = 0 
#     while queue :
#         x, y = queue.pop(0)

#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if nx < 0 or nx >= M or ny < 0 or ny >= N:
#                 continue

#             if arr[nx][ny] == 1:
#                 arr[nx][ny] = 0 
#                 queue.append([nx, ny])


# for _ in range(T) :
#     cnt =0 
#     M, N, K = map(int, input().split())
#     arr = [[0] * (N) for _ in range(M)]

#     #행렬 만들기
#     for _ in range(K) :
#         x, y = map(int, input().split())
#         arr[x][y] = 1

#     for x in range(M) :
#         for y in range(N) :
#             if arr[x][y] == 1:
#                 BFS(x, y)
#                 cnt += 1
#     print(cnt)