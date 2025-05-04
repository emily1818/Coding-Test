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
