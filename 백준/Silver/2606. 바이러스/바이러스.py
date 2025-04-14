import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

cnt = 0 

arr = [[0] * (N+1) for _ in range(N+1)]
arr_v = [0] * (N+1)

for _ in range(M) :
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1

def BFS(start) : 
    queue = [start] 

    while queue : 
        start = queue.pop(0)
        for idx, i in enumerate(arr[start]) :
            if i == 1 :
                queue.append(idx)
                arr_v[idx] = 1
                arr[start][idx] = 0 
                arr[idx][start] = 0 
        




for idx, i  in enumerate(arr[1]) :
    BFS(1)
                                                                                                  

cnt = 0 
for i in arr_v[2:] :
    cnt += i 

# print(arr_v)
print(cnt)
