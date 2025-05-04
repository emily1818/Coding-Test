n = int(input())
target = int(input())

arr = [[0] * n for _ in range(n)]

# 시계 방향: 상 → 우 → 하 → 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x = y = n // 2  # 중앙 시작
arr[x][y] = 1

cur = 2
length = 1
target_x = target_y = x

while cur <= n * n:
    for dir in range(4):  # 시계 방향 4방향
        for _ in range(length):
            x += dx[dir]
            y += dy[dir]
            if 0 <= x < n and 0 <= y < n:
                arr[x][y] = cur
                if cur == target:
                    target_x, target_y = x, y
                cur += 1
        if dir % 2 == 1:
            length += 1

# 출력
for row in arr:
    print(' '.join(map(str, row)))
print(target_x + 1, target_y + 1)

# import sys 

# input = sys.stdin.readline

# n = int(input())
# num = int(input())
# arr = [[0]*(n) for _ in range(n)]
# result_x  =0 
# result_y = 0 
# if n % 2 == 0 :
#     x = n//2 
#     y = n //2 -1

# else : 
#     x = n//2
#     y = n //2 

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# idx = 0 
# arr[x][y] = 1

# for i in range(2, n * n + 1) :    
#     nx = x + dx[idx]
#     ny = y + dy[idx]
    
#     if  arr[nx][ny] != 0 :
#         idx = idx -1
#         if idx == -1 :
#             idx = 3 
#         x = x + dx[idx]
#         y = y + dy[idx]
#         arr[x][y] = i 

#     else :
#         arr[nx][ny] = i
#         x = nx
#         y = ny

#     idx = idx +1 
#     if idx ==4 :
#         idx = 0 
#     if i == num : 
#         result_x = x
#         result_y = y


# for line in arr : 
#     print(" ".join(map(str, line)))
# print(result_x + 1, result_y + 1)