import sys
from collections import deque
input = sys.stdin.readline

# 입력
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 레이어 개수
layers = min(N, M) // 2

for layer in range(layers):
    elements = deque()

    top, left = layer, layer
    bottom, right = N - layer - 1, M - layer - 1

    # 한 레이어에서 반시계 방향으로 원소 뽑기
    # 위쪽
    for i in range(left, right):
        elements.append(arr[top][i])
    # 오른쪽
    for i in range(top, bottom):
        elements.append(arr[i][right])
    # 아래쪽
    for i in range(right, left, -1):
        elements.append(arr[bottom][i])
    # 왼쪽
    for i in range(bottom, top, -1):
        elements.append(arr[i][left])

    # 회전
    elements.rotate(-R)

    # 회전한 결과를 다시 배열에 넣기
    idx = 0
    for i in range(left, right):
        arr[top][i] = elements[idx]
        idx += 1
    for i in range(top, bottom):
        arr[i][right] = elements[idx]
        idx += 1
    for i in range(right, left, -1):
        arr[bottom][i] = elements[idx]
        idx += 1
    for i in range(bottom, top, -1):
        arr[i][left] = elements[idx]
        idx += 1

# 출력
for row in arr:
    print(' '.join(map(str, row)))
