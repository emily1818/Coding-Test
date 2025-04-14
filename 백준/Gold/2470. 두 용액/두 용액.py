

## 2470
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()


start = 0 
end = N-1
final = [start, end]
temp = abs(arr[start] + arr[end])



while start < end :
    result = arr[start] + arr[end]

    if abs(result) < temp :
        temp = abs(result)
        final = [start, end]
        if temp == 0  :
            break 
    if result < 0 : 
        start += 1
    else :
        end -=1 

    
print(arr[final[0]], arr[final[1]])