import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = str(input()).strip()

n_len = 2*n +1
arr_n = ""
cnt  =0 

for i in range(1, n_len+1) :
    if i % 2 == 1 :
        arr_n += "I"

    else :
        arr_n  += "O"


for start in range(m-n_len +1 ) :
    arr_s = s[start:start+n_len]
    if arr_n == arr_s :
        cnt+=1 


print(cnt)