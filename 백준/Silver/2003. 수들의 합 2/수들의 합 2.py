import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))


num_sum = 0 
cnt = 0 
start = 0 
end = 1


while end <= N and start <= end :
    nums_arr = arr[start:end]
    num_sum = sum(nums_arr)

    if num_sum == M :
        cnt += 1 
        start += 1
    elif num_sum < M :
        end +=1 
    else :
        start += 1

print(cnt)
