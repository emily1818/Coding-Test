import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
else:
    arr = [0] * (N+1)
    arr[1] = 1
    arr[2] = 3

    for i in range(3, N+1):
        arr[i] = arr[i-2] * 2 + arr[i-1]
    print(arr[N] % 10007)
