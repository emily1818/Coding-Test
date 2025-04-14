import sys
input = sys.stdin.readline

N =int(input())
arr_sq = (N) * [0]
arr_not_sq = (N) * [0]
arr = (N) * [0]

if N ==1 : 
    arr[0] = int(input())
elif N >=2 : 
    arr[0] = int(input())
    arr[1] = int(input())

    arr_sq[1] = arr[1] + arr[0]
    arr_not_sq[1] = arr[1]
    arr[1] = max(arr_sq[1], arr_not_sq[1])

for i in range(2, N) :
    arr[i] = int(input())
    arr_not_sq[i] = arr[i] + arr[i-2]
    arr_sq[i] = arr[i] + arr_not_sq[i-1]
    arr[i] = max(arr_sq[i], arr_not_sq[i])

print(arr[N-1])