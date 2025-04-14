import sys
input = sys.stdin.readline

T = int(input())

arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]  # 미리 10개 이상 생성

# 입력값 중 가장 큰 수까지 미리 계산
max_n = 0
inputs = []
for _ in range(T):
    n = int(input())
    inputs.append(n)
    if n > max_n:
        max_n = n

for i in range(len(arr), max_n + 1):
    arr.append(arr[i - 1] + arr[i - 5])

for n in inputs:
    print(arr[n])
