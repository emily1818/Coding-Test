import sys
input = sys.stdin.readline

T = int(input())

arr = [0] * 11
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(4, 11) :
    arr[i] = arr[i-3] + arr[i-2] + arr[i-1]
    
for _ in range(T) :
    num = int(input())
    print(arr[num])





# t = int(input())

# cnt = [0] * 11
# cnt[1] = 1
# cnt[2] = 2
# cnt[3] = 4

# for i in range(4, 11):
#     cnt[i] = cnt[i-3] + cnt[i-2] + cnt[i-1]

# for _ in range(t):
#     n = int(input())
#     print(cnt[n])