import sys

input = sys.stdin.readline

arr = []
result = ""
max_length = 0 

for _ in range(5) :
    word = list(input().strip())
    if len(word) > max_length :
        max_length = len(word)
    arr.append(word)


for i in range(max_length) :
    for j in range(5) :
        try : 
            result += arr[j][i]
        except : 
            continue

print(result)
    