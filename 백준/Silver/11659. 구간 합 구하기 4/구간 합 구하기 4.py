import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0 
arr_sum = [0] * (N)

for n in range(N) :
    sum = sum + arr[n]
    arr_sum[n] = sum

for _ in range(M) :
    i, j = map(int, input().split())
    if i == 1 : 
        result = arr_sum[j-1] 
    else : 
        result = arr_sum[j-1] - arr_sum[i-2]
    print(result)
#시간초과
# for _ in range(M) :
#     result = 0 
#     i, j = map(int, input().split())
#     for n in range(i, j+1):
#         result = result + arr[n-1]
#     print(result)