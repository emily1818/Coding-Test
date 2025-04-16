import sys

input = sys.stdin.readline
s = input().strip()
arr_s = {} #key : alpha value : cnt
odd_cnt = 0 
odd_index = 0 
odd_alpha = ""
result = ""

s_set = sorted(set(s))

for i in s_set :
    arr_s[i] = s.count(i)
    if arr_s[i] % 2 ==1 :
        odd_cnt +=1
        odd_alpha = i
    

if odd_cnt >=2 :
    print("I'm Sorry Hansoo")
else : 
    # 앞부분
    for i in arr_s :
        for _ in range(arr_s[i]//2) :
            result += i
    # 중간
    if odd_alpha : 
        result += odd_alpha
    # 뒷부분
    for i in reversed(arr_s):
        for _ in range(arr_s[i]//2) :
            result += i


    print(result)