import sys
input = sys.stdin.readline

N = map(int, input())
arr = list(map(int, input().split()))
ans = 0
waiting_time = 0 
#시간순대로 정렬
arr.sort()
for idx, i in enumerate(arr) :
    waiting_time = 0 
    for j in arr[:idx+1] :
        waiting_time += j
    ans += waiting_time
print(ans)