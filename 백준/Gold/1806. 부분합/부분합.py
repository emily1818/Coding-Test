## 1806
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0 
end = 0
result = 1000000000
sum_num =0 


while True :
    if sum_num >= S :
        temp = end - start
        if result > temp :
            result = temp
        sum_num -= arr[start]
        start += 1

    elif end == N :
        break
    else :
        sum_num += arr[end]
        end += 1

if result == 1000000000:
    print(0)
else : 

    print(result)
        



